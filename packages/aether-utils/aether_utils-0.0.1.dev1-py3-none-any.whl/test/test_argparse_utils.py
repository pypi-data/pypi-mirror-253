import json

from aether_utils.argparse_utils import json_loads_fixer


class TestJSONLoadFixer:
    def test_unquoted(self):
        sample_array = [0, 1, 2]
        argstring = json.dumps(sample_array)

        result = json_loads_fixer(argstring)
        assert result == sample_array

    def test_quoted(self):
        sample_array = [0, 1, 2]
        argstring = "'" + json.dumps(sample_array) + "'"

        result = json_loads_fixer(argstring)
        assert result == sample_array
