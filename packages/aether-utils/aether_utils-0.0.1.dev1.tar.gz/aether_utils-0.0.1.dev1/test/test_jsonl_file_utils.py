import pathlib

from aether_utils.jsonl_file_utils import (
    JSONLReader,
    JSONLWriter,
    load_jsonl,
    save_jsonl,
)


class TestWholeFile:
    def test_roundtrip(self, test_directory: pathlib.Path):
        my_data = [dict(a=1, b=2), dict(a=2, b=3)]

        target_file = test_directory / "my_test.jsonl"
        encoding = "utf-8-sig"

        assert not target_file.exists()
        save_jsonl(target_file, my_data, encoding)
        assert target_file.exists()

        loaded = load_jsonl(target_file, encoding)
        assert loaded == my_data


class TestByLine:
    def test_roundtrip(self, test_directory: pathlib.Path):
        my_data_0 = dict(c=1, d=2)

        target_file = test_directory / "my_test.jsonl"
        encoding = "utf-8-sig"

        assert not target_file.exists()
        with JSONLWriter(target_file, encoding) as jlf:
            jlf.write_line(my_data_0)
        assert target_file.exists()

        line_count = 0
        with JSONLReader(target_file, encoding) as jlf:
            for line in jlf:
                line_count += 1
                assert line == my_data_0
        assert line_count == 1

    def test_none_writer(self):
        my_data = [dict(e=1, f=2)]
        with JSONLWriter(None, "utf-8") as jlf:
            for item in my_data:
                jlf.write_line(item)
        # Would have to assert log message here....
