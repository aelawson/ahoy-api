from src.services.headers import Headers

class TestHeaders:

    def test_default_headers(self):
        data = b'abcdefg'
        expected_result = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(data)))
        ]
        actual_result = Headers.get_default_headers(data)
        assert actual_result == expected_result
