import dataclasses
import functools
import pathlib
import time
from enum import Enum
from typing import Any, Callable, Tuple

import joblib

from aether_utils.jsonl_file_utils import JSONLReader, JSONLWriter
from aether_utils.logging_utils import get_standard_logger_for_file

_logger = get_standard_logger_for_file(__file__)


class ItemState(Enum):
    Success = 0
    Failure = 1


@dataclasses.dataclass
class _MapResult:
    state: ItemState = ItemState.Success
    time: float = float()
    result: dict[str, Any] | None = None


def _map_wrapper(
    item: dict[str, Any],
    *,
    map_func: Callable[[dict[str, Any]], dict[str, Any] | None],
) -> _MapResult:
    _logger.info(f"Mapping :{item}")
    start = time.time()
    result = _MapResult()
    try:
        result.result = map_func(item)
        result.state = ItemState.Success
    except Exception as e:
        _logger.warning(f"Caught exception: {e}")
        result.result = item
        result.state = ItemState.Failure
    stop = time.time()
    result.time = stop - start
    return result


def line_map_parallel(
    *,
    map_func: Callable[[dict[str, Any]], dict[str, Any] | None],
    source_file: pathlib.Path,
    source_encoding: str,
    dest_file: pathlib.Path,
    dest_encoding: str,
    n_worker_tasks: int,
    error_file: pathlib.Path | None = None,
    error_encoding: str | None = None,
    max_errors: int = 5,
) -> Tuple[int, int]:
    actual_map_func = functools.partial(_map_wrapper, map_func=map_func)

    n_success = 0
    n_errors = 0
    all_times = []
    with JSONLReader(source_file, source_encoding) as jsonl_src:
        with JSONLWriter(dest_file, dest_encoding) as out_file:
            with JSONLWriter(error_file, error_encoding) as err_file:
                result = joblib.Parallel(
                    n_jobs=n_worker_tasks, return_as="generator", verbose=50
                )(joblib.delayed(actual_map_func)(x) for x in jsonl_src)
                for r in result:
                    assert isinstance(r, _MapResult)
                    all_times.append(r.time)
                    if r.state == ItemState.Success:
                        if r.result is not None:
                            out_file.write_line(r.result)
                        n_success += 1
                    else:
                        # r.result will always be the input item
                        err_file.write_line(r.result)
                        n_errors += 1
                        if n_errors > max_errors:
                            _logger.critical("Too many errors")
                            raise Exception("Too many errors. See log for details")
    _logger.info(f"Min Time : {min(all_times)}s")
    _logger.info(f"Mean Time: {sum(all_times)/len(all_times)}s")
    _logger.info(f"Max Time : {max(all_times)}s")
    _logger.info("line_map_parallel completed")

    return n_success, n_errors
