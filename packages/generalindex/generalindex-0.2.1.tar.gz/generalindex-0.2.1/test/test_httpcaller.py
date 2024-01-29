import os
import unittest
from io import BytesIO
from unittest import mock
from unittest.mock import Mock

from generalindex.HTTPCaller import HTTPCaller
from generalindex.exceptions import ApiResponseException

os.environ["NG_API_AUTHTOKEN"] = "test"


class ApiTestCase(unittest.TestCase):

    @mock.patch('requests.post')
    def test_given_response_200_when_post_then_returns_response(self, mock_requests):
        caller = HTTPCaller()
        mock_response = Mock()
        mock_requests.return_value = mock_response
        mock_response.status_code = 200

        response = caller.post("https://test.com")

        self.assertTrue(response is not None)

    @mock.patch('requests.post')
    def test_given_response_401_when_post_then_returns_response(self, mock_requests):
        caller = HTTPCaller()
        mock_response = Mock()
        mock_requests.return_value = mock_response
        mock_response.status_code = 401
        with self.assertRaises(ApiResponseException) as context:
            caller.post("https://test.com")

        self.assertTrue('Posting with message None ended with error ' in str(context.exception))

    @mock.patch('requests.post')
    def test_given_headers_when_post_then_updates_accordingly(self, mock_requests):
        caller = HTTPCaller()
        headers = {'Content-Type': 'text/plain'}
        headers_updated = {'Authorization': 'Bearer test', 'Content-Type': 'text/plain',
                           'User-Agent': 'GX_PythonSDK_V0.1.13'}
        mock_response = Mock()
        mock_requests.return_value = mock_response
        mock_response.status_code = 200

        response = caller.post("https://test.com", headers=headers)

        self.assertTrue(response is not None)
        calls = mock_requests.mock_calls
        self.assertDictEqual(
            calls[0].kwargs['headers'], headers_updated)

    @mock.patch('requests.Session')
    def test_given_headers_when_post_then_updates_accordingly(self, mock_session):
        caller = HTTPCaller()
        headers = {'Content-Type': 'text/plain'}
        headers_updated = {'Authorization': 'Bearer test', 'Content-Type': 'text/plain',
                           'User-Agent': 'GX_PythonSDK_V0.1.13'}
        response_mock = Mock()
        mock_session.return_value.get.return_value = response_mock
        response_mock.url = 'test'
        response_mock.status_code = 200

        response = caller.get("https://test.com", headers=headers)

        self.assertTrue(response is not None)
        self.assertEqual(mock_session.return_value.mount.call_count, 2)
        calls = mock_session.return_value.get.mock_calls
        self.assertDictEqual(
            calls[0].kwargs['headers'], headers_updated)

    @mock.patch('requests.Session')
    def test_given_401_when_post_then_updates_accordingly(self, mock_session):
        caller = HTTPCaller()
        headers = {'Content-Type': 'text/plain'}
        headers_updated = {'Authorization': 'Bearer test', 'Content-Type': 'text/plain',
                           'User-Agent': 'GX_PythonSDK_V0.1.13'}
        response_mock = Mock()
        mock_session.return_value.get.return_value = response_mock
        response_mock.url = 'test'
        response_mock.status_code = 401

        with self.assertRaises(ApiResponseException) as context:
            caller.get("https://test.com", headers=headers)
            self.assertEqual(mock_session.return_value.mount.call_count, 2)
            calls = mock_session.return_value.get.mock_calls
            self.assertDictEqual(
                calls[0].kwargs['headers'], headers_updated)

        self.assertTrue('Data reception from https://test.com ended with error' in str(context.exception))

    @mock.patch('requests.Session')
    @mock.patch('requests.put')
    @mock.patch('requests.post')
    def test_given_file_when_upload_then_returns_id(self, mock_post, mock_put, mock_session):
        caller = HTTPCaller()
        file_name = "test.json"
        p_u = [
            {"name": "PARTIAL_UPDATE", "value": "true"},
            {"name": "AVOID_DUPLICATES", "value": "true"}]
        payload = {"groupName": "group_name",
                   "fileName": file_name,
                   "fileType": "SOURCE",
                   "fields": p_u}

        headers = {'Content-Type': 'text/plain'}
        headers_updated = {'Authorization': 'Bearer test', 'Content-Type': 'text/plain',
                           'User-Agent': 'GX_PythonSDK_V0.1.13'}
        file = BytesIO(bytes("{tes:v}", 'utf-8'))
        post_response_mock = Mock()
        put_response_mock = Mock()
        get_response_mock = Mock()
        mock_post.return_value = post_response_mock
        post_response_mock.status_code = 200
        file_id = 12
        post_response_mock.json.return_value = {
            'location': 1,
            'fileId': file_id
        }
        mock_put.return_value = put_response_mock
        put_response_mock.status_code = 200

        mock_session.return_value.get.return_value = get_response_mock
        get_response_mock.status_code = 200
        get_response_mock.json.return_value = {
            'items': [
                {"item1": 1},
                {"item2": 2}
            ],

        }
        response = caller.file_uploader(payload=payload, file=file, headers=headers)

        self.assertEqual(response, file_id)
        calls = mock_post.mock_calls
        self.assertDictEqual(
            calls[0].kwargs['headers'], headers_updated)

    @mock.patch('requests.Session')
    def test_given_file_not_uploaded_when_upload_then_raises_exc(self, mock_session):
        caller = HTTPCaller()
        get_response_mock = Mock()
        mock_session.return_value.get.return_value = get_response_mock
        get_response_mock.status_code = 200
        get_response_mock.json.return_value = {
            'items': [],
        }

        result = caller.check_upload_successful(avoid_duplicates=False, file_id='12',
                                                uploaded_file_check_retries=1)

        self.assertEqual(result, False)

    @mock.patch('requests.Session')
    def test_avoid_duplicates_not_uploaded_when_upload_then_raises_exc(self, mock_session):
        caller = HTTPCaller()
        get_response_mock = Mock()
        mock_session.return_value.get.return_value = get_response_mock
        get_response_mock.status_code = 200
        get_response_mock.json.return_value = {
            'items': [],
        }

        result = caller.check_upload_successful(avoid_duplicates=True, file_id='12',
                                                uploaded_file_check_retries=1)

        self.assertTrue(result)


@mock.patch('requests.Session')
@mock.patch('requests.put')
@mock.patch('requests.post')
def test_given_wrong_file_when_upload_then_raise_exc(self, mock_post, mock_put, mock_session):
    caller = HTTPCaller()
    post_response_mock = Mock()

    mock_post.return_value = post_response_mock
    post_response_mock.status_code = 200
    file_id = 12
    post_response_mock.json.return_value = {
        'location': 1,
        'fileId': file_id
    }
    with self.assertRaises(TypeError) as context:
        caller.file_uploader(payload=None, file=123)

    self.assertTrue(
        'Passed file argument must be either a file path to a file saved on the disk, either a io.BytesIO object to stream from memory' in str(
            context.exception))


def test_given_avoid_duplicates_return_true(self):
    caller = HTTPCaller()

    p_u = [
        {"name": "PARTIAL_UPDATE", "value": "true"},
        {"name": "AVOID_DUPLICATES", "value": "true"}]

    payload = {"fields": p_u}
    self.assertTrue(caller.is_avoid_duplicates(payload))


def test_given_not_avoid_duplicates_return_true(self):
    caller = HTTPCaller()
    p_u = [{"name": "AVOID_DUPLICATES", "value": "false"},
           {"name": "PARTIAL_UPDATE", "value": "true"}]
    payload = {"fields": p_u}
    self.assertEqual(caller.is_avoid_duplicates(payload), False)
