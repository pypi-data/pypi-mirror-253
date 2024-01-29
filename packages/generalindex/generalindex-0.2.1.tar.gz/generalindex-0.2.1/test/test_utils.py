import os
import unittest

from generalindex.utils import PathFormatter
from generalindex.exceptions import MissingArgumentException

os.environ["NG_API_AUTHTOKEN"] = "test"


class UtilsTestCase(unittest.TestCase):

    def test_no_params_when_get_symbols_then_raises_exc(self):
        formatter = PathFormatter()
        with self.assertRaises(MissingArgumentException) as context:
            formatter.get_symbol_queried_path()

        self.assertTrue(
            'Please specify either group_name or search_for parameter of get_symbols() method'
            in str(context.exception))

    def test_ggiven_group_name_when_get_symbols_then_parses_correctly(self):
        formatter = PathFormatter()

        response = formatter.get_symbol_queried_path(group_name="MyGroup")
        self.assertTrue(response is not None)
        self.assertEqual(response, '/ts/symbol/search?size=1000&from=0&query=groupName.keyword%3DMyGroup')

    def test_given_search_for_when_get_symbols_then_parses_correctly(self):
        formatter = PathFormatter()

        response = formatter.get_symbol_queried_path(search_for="symbols.code=GX0000001")
        self.assertTrue(response is not None)
        self.assertEqual(response, '/ts/symbol/search?size=1000&from=0&query=symbols.code%3DGX0000001')

    def test_given_both_when_get_symbols_then_parses_correctly(self):
        formatter = PathFormatter()

        response = formatter.get_symbol_queried_path(group_name="MyGroup", search_for="symbols.code=GX0000001")
        self.assertTrue(response is not None)
        self.assertEqual(response,
                         '/ts/symbol/search?size=1000&from=0&query=symbols.code%3DGX0000001*%26groupName.keyword%3DMyGroup')
