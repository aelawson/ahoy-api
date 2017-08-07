from src.services.response import Response

class TestResponse:

    def test_response_init(self):
        response = {}
        def start_response(status, headers):
            response['status'] = status
            response['headers'] = headers

        response_body = Response.response(start_response)

        assert response['status'] == '200 OK'
        assert response['headers'] == [
            ('Content-Type', 'text/plain'),
            ('Content-Length', '0')
        ]
        assert response_body == [b'']

    def test_response_init_status_code(self):
        response = {}
        def start_response(status, headers):
            response['status'] = status
            response['headers'] = headers

        response_body = Response.response(
            start_response,
            status_code=200
        )

        assert response['status'] == '200 OK'
        assert response['headers'] == [
            ('Content-Type', 'text/plain'),
            ('Content-Length', '0')
        ]
        assert response_body == [b'']

    def test_response_init_headers(self):
        response = {}
        def start_response(status, headers):
            response['status'] = status
            response['headers'] = headers

        headers = [
            ('Content-Type', 'application/json'),
            ('Content-Length', '100')
        ]
        response_body = Response.response(
            start_response,
            headers=headers
        )

        assert response['status'] == '200 OK'
        assert response['headers'] == [
            ('Content-Type', 'application/json'),
            ('Content-Length', '100')
        ]
        assert response_body == [b'']

    def test_response_init_body(self):
        response = {}
        def start_response(status, headers):
            response['status'] = status
            response['headers'] = headers

        body = b'Hello World!'
        response_body = Response.response(
            start_response,
            body=body
        )

        assert response['status'] == '200 OK'
        assert response['headers'] == [
            ('Content-Type', 'text/plain'),
            ('Content-Length', '12')
        ]
        assert response_body == [b'Hello World!']
