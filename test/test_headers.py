from src.services.headers import Headers
from test.utils import compare_sorted

class TestHeaders:

    def test_default_headers_no_body(self):
        expected_result = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', "0")
        ]
        actual_result = Headers.construct_headers()

        assert compare_sorted(actual_result, expected_result)

    def test_default_headers_with_body(self):
        body = b'abcdefg'
        expected_result = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(body)))
        ]
        actual_result = Headers.construct_headers(body=body)

        assert compare_sorted(actual_result, expected_result)

    def test_headers_no_body(self):
        headers = {
            'test-header': 'value',
            'Content-Type': 'application/json'
        }
        expected_result = [
            ('Content-Type', 'application/json'),
            ('test-header', 'value'),
            ('Content-Length', "0")
        ]
        actual_result = Headers.construct_headers(headers=headers)

        assert compare_sorted(actual_result, expected_result)

    def test_headers_with_body(self):
        body = b'abcdefg'
        headers = {
            'test-header': 'value',
            'Content-Type': 'application/json'
        }
        expected_result = [
            ('Content-Type', 'application/json'),
            ('test-header', 'value'),
            ('Content-Length', str(len(body)))
        ]
        actual_result = Headers.construct_headers(headers=headers, body=body)

        assert compare_sorted(actual_result, expected_result)