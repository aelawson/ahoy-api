from src.services.headers import Headers

class TestHeaders:

    @staticmethod
    def header_key(header):
        return header[0]

    @staticmethod
    def compare_sorted(actual, expected):
        actual = sorted(actual, key=TestHeaders.header_key)
        expected = sorted(expected, key=TestHeaders.header_key)
        return actual == expected

    def test_default_headers_no_body(self):
        expected_result = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', "0")
        ]
        actual_result = Headers.construct_headers()

        assert TestHeaders.compare_sorted(actual_result, expected_result)

    def test_default_headers_with_body(self):
        body = b'abcdefg'
        expected_result = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(body)))
        ]
        actual_result = Headers.construct_headers(body=body)

        assert TestHeaders.compare_sorted(actual_result, expected_result)

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

        assert TestHeaders.compare_sorted(actual_result, expected_result)

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

        assert TestHeaders.compare_sorted(actual_result, expected_result)