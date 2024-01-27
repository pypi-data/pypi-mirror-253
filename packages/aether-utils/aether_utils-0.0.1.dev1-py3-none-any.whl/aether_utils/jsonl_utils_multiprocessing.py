import dataclasses
import multiprocessing
import pathlib
import queue
import time
import traceback
from typing import Tuple

from .jsonl_file_utils import JSONLReader, JSONLWriter
from .logging_utils import get_logger_for_process, get_standard_logger_for_file

_logger = get_standard_logger_for_file(__file__)


class ItemMapper:
    def __init__(self):
        pass

    def start_up(self, worker_id: int) -> None:
        pass

    def shutdown(self) -> None:
        pass

    def map(self, item: dict[str, any]) -> dict[str, any] | None:
        raise NotImplementedError("map invoked on ItemMapper")


class _WorkCompleteMarker:
    def __init__(self, message: str):
        self._message = message

    @property
    def message(self) -> str:
        return self._message


@dataclasses.dataclass
class RunStats:
    success_count: int = int()
    failure_count: int = int()


def _enqueue_from_jsonl_worker(
    *,
    source_file: pathlib.Path,
    source_encoding: str,
    target_queue: multiprocessing.Queue,
    n_complete_markers: int,
):
    logger = get_logger_for_process(__file__, "enqueue")
    logger.info("Starting")

    lines_read = 0
    with JSONLReader(source_file, source_encoding) as in_file:
        for nxt in in_file:
            logger.debug(f"Reading line {lines_read}")
            target_queue.put(nxt)
            lines_read += 1

    for i in range(n_complete_markers):
        logger.info(f"WorkerCompleteMarker {i}")
        nxt_marker = _WorkCompleteMarker(f"Completion marker {i}")
        target_queue.put(nxt_marker)
    logger.info("Completed")


def _dequeue_to_jsonl_worker(
    *,
    dest_file: pathlib.Path,
    dest_encoding: str,
    target_queue: multiprocessing.Queue,
    n_complete_markers_expected: int,
):
    logger = get_logger_for_process(__file__, "output")
    logger.info("Starting")

    n_complete_markers_seen = 0

    with JSONLWriter(dest_file, dest_encoding) as out_file:
        while n_complete_markers_seen < n_complete_markers_expected:
            nxt_item = target_queue.get()
            if isinstance(nxt_item, _WorkCompleteMarker):
                logger.info(f"Got WorkCompleteMarker '{nxt_item.message}'")
                n_complete_markers_seen += 1
            else:
                logger.debug("Writing item")
                out_file.write_line(nxt_item)


def _error_to_jsonl_worker(
    *,
    error_file: pathlib.Path | None,
    error_encoding: str | None,
    target_queue: multiprocessing.Queue,
    n_complete_markers_expected: int,
    n_errors_max: int,
):
    logger = get_logger_for_process(__file__, "error")
    logger.info("Starting")

    n_complete_markers_seen = 0
    n_errors_seen = 0

    with JSONLWriter(error_file, error_encoding) as err_file:
        while n_complete_markers_seen < n_complete_markers_expected:
            nxt_item = target_queue.get()

            if isinstance(nxt_item, _WorkCompleteMarker):
                logger.info(f"Got WorkCompleteMarker '{nxt_item.message}'")
                n_complete_markers_seen += 1
            else:
                n_errors_seen += 1
                logger.warning(f"Received Error Item (total={n_errors_seen})")
                err_file.write_line(nxt_item)

            if n_errors_seen > n_errors_max:
                logger.fatal(f"Error limit of {n_errors_max} exceeded")
                logger.fatal(f"Final item: {nxt_item}")
                # This will kill the process
                raise ValueError(
                    f"Too many error items ({n_errors_seen} > {n_errors_max})"
                )
        logger.info("About to close error file")


def _monitor_worker(
    *,
    source_queue: multiprocessing.Queue,
    dest_queue: multiprocessing.Queue,
    worker_time_queue: multiprocessing.Queue,
    n_complete_markers_expected: int,
    update_seconds: int,
):
    logger = get_logger_for_process(__file__, "monitor")
    logger.info("Starting")
    all_times = []

    n_complete_markers_seen = 0
    while n_complete_markers_seen < n_complete_markers_expected:
        time.sleep(update_seconds / (1 + n_complete_markers_seen))
        src_count = source_queue.qsize()
        dst_count = dest_queue.qsize()

        # Since qsize() is not reliable for multiprocessing, have a
        # slightly unpleasant pattern here
        try:
            while True:
                fetched = worker_time_queue.get_nowait()
                if isinstance(fetched, _WorkCompleteMarker):
                    n_complete_markers_seen += 1
                else:
                    all_times.append(fetched)
        except queue.Empty:
            pass

        min_time = -1
        max_time = -1
        mean_time = -1
        if len(all_times) > 0:
            min_time = min(all_times)
            max_time = max(all_times)
            mean_time = sum(all_times) / len(all_times)

        logger.info(f"Items in Source Queue: {src_count}")
        logger.info(f"Items in Destination Queue: {dst_count}")
        logger.info(f"Items processed so far: {len(all_times)}")
        logger.info(
            f"Times: {min_time:.2f}s (min) {mean_time:.2f}s (mean) {max_time:.2f}s"
            " (max)"
        )
    logger.info("Completed")


def _queue_worker(
    *,
    mapper_obj: ItemMapper,
    source_queue: multiprocessing.Queue,
    dest_queue: multiprocessing.Queue,
    error_queue: multiprocessing.Queue,
    run_stats_queue: multiprocessing.Queue,
    worker_time_queue: multiprocessing.Queue,
    id: int,
):
    logger = get_logger_for_process(__file__, f"worker{id:02}")
    logger.info("Starting")

    mapper_obj.start_up(id)
    logger.info("Completed worker startup")

    done = False
    success_count = 0
    failure_count = 0
    while not done:
        nxt_item = source_queue.get()

        if isinstance(nxt_item, _WorkCompleteMarker):
            logger.info(f"Got WorkCompleteMarker '{nxt_item.message}'")
            done = True
        else:
            logger.debug("Processing item")
            start_time = time.time()
            try:
                nxt_result = mapper_obj.map(nxt_item)
                stop_time = time.time()
                if nxt_result is not None:
                    dest_queue.put(nxt_result)
                else:
                    logger.debug("map_func returned None")
                success_count += 1
            except Exception as e:
                stop_time = time.time()
                logger.warn(f"Item failed: {e}\n{traceback.format_exception(e)}")
                error_queue.put(nxt_item)
                failure_count += 1
            worker_time_queue.put(stop_time - start_time)
    logger.info("Completed work items")
    marker = _WorkCompleteMarker(f"queue_worker{id:02}")
    dest_queue.put(marker)
    error_queue.put(marker)
    worker_time_queue.put(marker)
    stats = RunStats(success_count=success_count, failure_count=failure_count)
    run_stats_queue.put(stats)
    logger.info("Queues updated")
    mapper_obj.shutdown()
    _logger.info("Exiting")


def line_map_mp(
    *,
    mapper: ItemMapper,
    source_file: pathlib.Path,
    source_encoding: str,
    dest_file: pathlib.Path,
    dest_encoding: str,
    n_worker_tasks: int,
    error_file: pathlib.Path | None = None,
    error_encoding: str | None = None,
    max_errors: int = 5,
    update_seconds: int = 30,
) -> Tuple[int, int]:
    """Apply `mapper` to every line in `source_file`.

    This is a variation of `line_map` which uses multiple
    workers (from `multiprocessing`) to perform the map.
    Note that the order of the lines in `dest_file` is
    undefined.
    If you need to match lines at a later point in your
    processing, you should include an `id` field on each
    line.
    The `mapper` object needs to be subclassed and its
    `map()` method implemented
    """
    _logger.info("Starting line_map_mp")

    assert source_file.exists()
    assert isinstance(mapper, ItemMapper)

    source_queue = multiprocessing.Queue(maxsize=2 * n_worker_tasks)
    dest_queue = multiprocessing.Queue(maxsize=2 * n_worker_tasks)
    error_queue = multiprocessing.Queue(maxsize=2 * n_worker_tasks)

    run_stats_queue = multiprocessing.Queue(maxsize=n_worker_tasks)
    timing_queue = multiprocessing.Queue()

    # List of the various processes spawned
    # This will _not_ include the error output worker

    worker_processes = []

    # Setup the enqueuer
    enqueue_process = multiprocessing.Process(
        target=_enqueue_from_jsonl_worker,
        kwargs=dict(
            source_file=source_file,
            source_encoding=source_encoding,
            target_queue=source_queue,
            n_complete_markers=n_worker_tasks,
        ),
        name="Enqueuer",
    )
    worker_processes.append(enqueue_process)

    # Setup the workers
    for i in range(n_worker_tasks):
        nxt = multiprocessing.Process(
            target=_queue_worker,
            kwargs=dict(
                mapper_obj=mapper,
                source_queue=source_queue,
                dest_queue=dest_queue,
                error_queue=error_queue,
                run_stats_queue=run_stats_queue,
                worker_time_queue=timing_queue,
                id=i,
            ),
            name=f"Worker {i}",
        )
        worker_processes.append(nxt)

    # Setup  the monitor
    monitor_process = multiprocessing.Process(
        target=_monitor_worker,
        kwargs=dict(
            source_queue=source_queue,
            dest_queue=dest_queue,
            worker_time_queue=timing_queue,
            n_complete_markers_expected=n_worker_tasks,
            update_seconds=update_seconds,
        ),
        name="Monitor",
    )
    worker_processes.append(monitor_process)

    # Setup the output dequeuer
    dequeue_output_process = multiprocessing.Process(
        target=_dequeue_to_jsonl_worker,
        kwargs=dict(
            dest_file=dest_file,
            dest_encoding=dest_encoding,
            target_queue=dest_queue,
            n_complete_markers_expected=n_worker_tasks,
        ),
        name="Output",
    )
    worker_processes.append(dequeue_output_process)

    # Start the error dequeuer
    dequeue_error_output_process = multiprocessing.Process(
        target=_error_to_jsonl_worker,
        kwargs=dict(
            error_file=error_file,
            error_encoding=error_encoding,
            target_queue=error_queue,
            n_complete_markers_expected=n_worker_tasks,
            n_errors_max=max_errors,
        ),
        name="Error Output",
    )
    dequeue_error_output_process.start()

    # Start the workers
    for wp in worker_processes:
        wp.start()

    # Wait for processes to complete

    # Check on errors first, since we may want to kill everything
    dequeue_error_output_process.join()
    if dequeue_error_output_process.exitcode != 0:
        _logger.critical(
            "Detected non-zero exit from dequeue_error_output_process:"
            f" {dequeue_error_output_process.exitcode}"
        )
        for wp in worker_processes:
            wp.kill()
        _logger.critical("Worker processes terminated")
        raise Exception("Too many errors. See log for details")

    # Do a normal exit
    _logger.info("Joining workers")
    for wp in worker_processes:
        wp.join()

    total_successes = 0
    total_failures = 0
    for _ in range(n_worker_tasks):
        nxt: RunStats = run_stats_queue.get()
        total_successes += nxt.success_count
        total_failures += nxt.failure_count

    _logger.info(f"Total Successful items: {total_successes}")
    _logger.info(f"Total Failed items    : {total_failures}")
    _logger.info("line_map_mp completed")
    return total_successes, total_failures
