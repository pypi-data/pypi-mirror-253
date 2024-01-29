import os
import unittest
from unittest.mock import Mock, patch

from generalindex.DatalakeHandler import DatalakeHandler

os.environ["NG_API_AUTHTOKEN"] = "test"


class DatalakeHandlerTestCase(unittest.TestCase):
    def test_given_avoid_duplicates_when_upload_file_returns_with_fields(self):
        dh = DatalakeHandler()
        mock_caller = Mock()
        test_id = "test_id"
        mock_caller.file_uploader.side_effect = [test_id]
        with patch.object(dh, "caller", new=mock_caller):
            result = dh.upload_file("Test,File,Content", "test_group", "test.csv", 'SOURCE', avoid_duplicates=True)
            calls = mock_caller.mock_calls
            self.assertTrue(result[0] is not None)
            self.assertTrue(result[0] == test_id)
            self.assertTrue(calls[0].args[0]['fields'][0]['name'] == "AVOID_DUPLICATES")
            self.assertTrue(calls[0].args[0]['fields'][0]['value'] == 'true')
    def test_given_partial_update_when_upload_file_returns_with_fields(self):
        dh = DatalakeHandler()
        mock_caller = Mock()
        test_id = "test_id"
        mock_caller.file_uploader.side_effect = [test_id]
        with patch.object(dh, "caller", new=mock_caller):
            result = dh.upload_file("Test,File,Content", "test_group", "test.csv", 'SOURCE', partial_update=True)
            calls = mock_caller.mock_calls
            self.assertTrue(result[0] is not None)
            self.assertTrue(result[0] == test_id)
            self.assertTrue(calls[0].args[0]['fields'][0]['name'] == "PARTIAL_UPDATE")
            self.assertTrue(calls[0].args[0]['fields'][0]['value'] == 'true')
