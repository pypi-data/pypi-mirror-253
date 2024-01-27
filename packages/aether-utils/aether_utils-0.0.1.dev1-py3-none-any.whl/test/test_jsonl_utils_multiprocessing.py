import pathlib

import pytest

from aether_utils.jsonl_file_utils import load_jsonl, save_jsonl
from aether_utils.jsonl_utils_multiprocessing import ItemMapper, line_map_mp


class SimpleMapper(ItemMapper):
    def __init__(self):
        super().__init__()

    def start_up(self, worker_id: int) -> None:
        print(f"Called start_up for {worker_id}")

    def map(self, item: dict[str, int]) -> dict[str, int] | None:
        if item["a"] == 1:
            raise ValueError("Raising for 1")
        if item["a"] == 2:
            return None
        return item


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

        mapper_object = SimpleMapper()

        success, failure = line_map_mp(
            mapper=mapper_object,
            source_file=input_file,
            dest_file=output_file,
            source_encoding=encoding,
            dest_encoding=encoding,
            error_file=error_file,
            error_encoding=encoding,
            n_worker_tasks=2,
            max_errors=1,
            update_seconds=1,
        )

        assert success == 5
        assert failure == 1

        output_data = load_jsonl(output_file, encoding)
        assert len(output_data) == 4

        seen_values = []
        expected_values = [0, 3, 4, 5]
        for item in output_data:
            assert isinstance(item, dict)
            seen_values.append(item["a"])
        assert sorted(seen_values) == expected_values

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

        mapper_object = SimpleMapper()

        with pytest.raises(Exception) as ve:
            _, _ = line_map_mp(
                mapper=mapper_object,
                source_file=input_file,
                dest_file=output_file,
                source_encoding=encoding,
                dest_encoding=encoding,
                error_file=error_file,
                error_encoding=encoding,
                n_worker_tasks=2,
                max_errors=1,
            )
        assert ve.value.args[0] == "Too many errors. See log for details"
