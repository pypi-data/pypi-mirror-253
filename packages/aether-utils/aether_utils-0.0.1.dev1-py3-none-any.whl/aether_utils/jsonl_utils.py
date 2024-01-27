import pathlib
import traceback
from typing import Any, Callable, Tuple

from .jsonl_file_utils import JSONLReader, JSONLWriter
from .logging_utils import get_standard_logger_for_file

_logger = get_standard_logger_for_file(__file__)


def line_map(
    *,
    map_func: Callable[[dict[str, Any]], dict[str, Any] | None],
    source_file: pathlib.Path,
    dest_file: pathlib.Path,
    source_encoding: str,
    dest_encoding: str,
    error_file: pathlib.Path | None = None,
    error_encoding: str | None = None,
    max_errors: int = -1,
) -> Tuple[int, int]:
    """Iterate over a JSONL file, applying `map_func` to each line.

    The result is stored in `dest_file` (as JSONL), and any lines
    which cause `map_func` to throw an exception will be stored
    in the JSONL `error_file` (if not None).
    If more than `max_errors` occur, then the whole function
    will abort.

    If `map_func` returns None for any line, then it will be
    omitted from the `dest_file`.
    """
    assert source_file.exists()

    successful_lines = 0
    skipped_lines = 0
    error_lines = 0
    with JSONLReader(source_file, source_encoding) as in_file:
        with JSONLWriter(dest_file, dest_encoding) as out_file:
            with JSONLWriter(error_file, error_encoding) as err_file:
                current_line = 0
                for nxt in in_file:
                    _logger.debug(f"Processing line: {current_line}")
                    try:
                        nxt_output = map_func(nxt)
                        if nxt_output is not None:
                            out_file.write_line(nxt_output)
                        else:
                            skipped_lines += 1
                            _logger.debug("Skipping because map_func returned 'None'")
                        successful_lines += 1
                    except Exception as e:
                        _logger.warning(
                            f"Caught exception: {e}\n{traceback.format_exception(e)}"
                        )
                        err_file.write_line(nxt)
                        error_lines += 1
                    current_line += 1

                    if max_errors > 0 and error_lines > max_errors:
                        raise ValueError(f"Terminating after {error_lines} errors")
    _logger.info(
        f"line_map complete ({successful_lines} successes (of which"
        f" {skipped_lines} skipped), {error_lines} failures)"
    )
    return successful_lines, error_lines


def line_reduce(
    *,
    reducer: Callable[[dict[str, Any]], None],
    source_file: pathlib.Path,
    source_encoding: str,
):
    """Call the `reducer` on every line in the `source_file`."""
    assert source_file.exists()

    with JSONLReader(source_file, source_encoding) as in_file:
        current_line = 0
        for nxt in in_file:
            _logger.debug(f"Processing line: {current_line}")
            current_line += 1
            _logger.debug("Calling reducer")
            reducer(nxt)
    _logger.info("line_reduce complete")
