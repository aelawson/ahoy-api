from src.services.response import Response

class TestResponse:

    def test_response_init(self):
        response_case = Response()
        assert response_case.status == {
            'status': '200 OK'
        }
        assert response_case.headers == [
            ('Content-Type', 'text/plain'),
            ('Content-Length', '0')
        ]
        assert response_case.body == b''

    def test_response_init_status_code(self):
        response_case = Response(status_code=200)
        assert response_case.status == {
            'status': '200 OK'
        }
        assert response_case.headers == [
            ('Content-Type', 'text/plain'),
            ('Content-Length', '0')
        ]
        assert response_case.body == b''

    def test_response_init_headers(self):
        headers = [
            ('Content-Type', 'application/json'),
            ('Content-Length', '100')
        ]
        response_case = Response(headers=headers)
        assert response_case.status == {
            'status': '200 OK'
        }
        assert response_case.headers == [
            ('Content-Type', 'application/json'),
            ('Content-Length', '100')
        ]
        assert response_case.body == b''

    def test_response_init_body(self):
        body = b'Hello World!'
        response_case = Response(body=body)
        assert response_case.status == {
            'status': '200 OK'
        }
        assert response_case.headers == [
            ('Content-Type', 'text/plain'),
            ('Content-Length', '12')
        ]
        assert response_case.body == b'Hello World!'
