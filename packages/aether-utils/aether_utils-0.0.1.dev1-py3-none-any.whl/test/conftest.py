import pathlib
import tempfile

import pytest


@pytest.fixture()
def test_directory() -> pathlib.Path:
    with tempfile.TemporaryDirectory() as test_directory:
        yield (pathlib.Path(test_directory))
