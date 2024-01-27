import pathlib

import pytest

from aether_utils.jsonl_file_utils import load_jsonl, save_jsonl
from aether_utils.jsonl_utils import line_map, line_reduce


def simple_mapper(item: dict[str, int]) -> dict[str, int] | None:
    if item["a"] == 1:
        raise ValueError("Raising for 1")
    if item["a"] == 2:
        return None
    return item


class SimpleAccumulator:
    def __init__(self):
        self.sum = 0

    def accumulate(self, item: dict[str, any]) -> None:
        self.sum += item["a"]


class TestLineMap:
    def test_smoke(self, test_directory: pathlib.Path):
        input_data = [dict(a=i) for i in range(6)]

        input_file = test_directory / "input.jsonl"
        output_file = test_directory / "output.jsonl"
        error_file = test_directory / "errors.jsonl"
        encoding = "utf-8-sig"

        save_jsonl(input_file, input_data, encoding)
        assert not output_file.exists()
        assert not error_file.exists()

        success, failure = line_map(
            map_func=simple_mapper,
            source_file=input_file,
            dest_file=output_file,
            source_encoding=encoding,
            dest_encoding=encoding,
            error_file=error_file,
            error_encoding=encoding,
            max_errors=1,
        )

        assert success == 5
        assert failure == 1

        output_data = load_jsonl(output_file, encoding)
        assert len(output_data) == 4
        for i, item in enumerate(output_data):
            assert isinstance(item, dict)
            if i == 0:
                assert item["a"] == i
            else:
                assert item["a"] == i + 2

        error_data = load_jsonl(error_file, encoding)
        assert len(error_data) == 1
        assert error_data[0]["a"] == 1

    def test_too_many_errors(self, test_directory: pathlib.Path):
        input_data = [dict(a=1) for _ in range(6)]

        input_file = test_directory / "input.jsonl"
        output_file = test_directory / "output.jsonl"
        error_file = test_directory / "errors.jsonl"
        encoding = "utf-8-sig"

        save_jsonl(input_file, input_data, encoding)
        assert not output_file.exists()
        assert not error_file.exists()

        with pytest.raises(ValueError) as ve:
            _, _ = line_map(
                map_func=simple_mapper,
                source_file=input_file,
                dest_file=output_file,
                source_encoding=encoding,
                dest_encoding=encoding,
                error_file=error_file,
                error_encoding=encoding,
                max_errors=1,
            )
        assert ve.value.args[0] == "Terminating after 2 errors"


class TestLineReduce:
    def test_smoke(self, test_directory: pathlib.Path):
        input_data = [dict(a=i) for i in range(6)]

        input_file = test_directory / "input.jsonl"
        encoding = "utf-8-sig"

        save_jsonl(input_file, input_data, encoding)

        reducer = SimpleAccumulator()

        line_reduce(
            reducer=reducer.accumulate, source_file=input_file, source_encoding=encoding
        )

        assert reducer.sum == 15
