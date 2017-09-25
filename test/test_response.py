from src.services.response import Response
from test.utils import compare_sorted

class TestResponse:

    def test_response_init(self):
        response = {}
        def start_response(status, headers):
            response['status'] = status
            response['headers'] = headers

        response_body = Response.response(start_response)

        expected_body = [b'']
        expected_status = '200 OK'
        expected_headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', '0')
        ]

        compare_sorted(response['status'], expected_status)
        compare_sorted(response['headers'], expected_headers)
        assert response_body == expected_body

    def test_response_init_status_code(self):
        response = {}
        def start_response(status, headers):
            response['status'] = status
            response['headers'] = headers

        response_body = Response.response(
            start_response,
            status_code=200
        )

        expected_body = [b'']
        expected_status = '200 OK'
        expected_headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', '0')
        ]

        compare_sorted(response['status'], expected_status)
        compare_sorted(response['headers'], expected_headers)
        assert response_body == expected_body

    def test_response_init_headers(self):
        response = {}
        def start_response(status, headers):
            response['status'] = status
            response['headers'] = headers

        headers = {
            'Content-Type': 'application/json',
            'Content-Length': '100'
        }
        response_body = Response.response(
            start_response,
            headers=headers
        )

        expected_body = [b'']
        expected_status = '200 OK'
        expected_headers = [
            ('Content-Type', 'application/json'),
            ('Content-Length', '100')
        ]

        compare_sorted(response['status'], expected_status)
        compare_sorted(response['headers'], expected_headers)
        assert response_body == expected_body

    def test_response_init_body(self):
        response = {}
        def start_response(status, headers):
            response['status'] = status
            response['headers'] = headers

        body = 'Hello World!'
        response_body = Response.response(
            start_response,
            body=body
        )

        expected_body = [b'Hello World!']
        expected_status = '200 OK'
        expected_headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', '0')
        ]

        compare_sorted(response['status'], expected_status)
        compare_sorted(response['headers'], expected_headers)
        assert response_body == expected_body
