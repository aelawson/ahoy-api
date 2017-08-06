from src.services.status_codes import StatusCodes

class TestStatusCodes:

    def test_get_status_code_success(self):
        status_code = 200
        expected_result = {
            'status': '200 OK'
        }
        actual_result = StatusCodes.get_status_message(status_code)
        assert actual_result == expected_result

    def test_get_status_code_fail(self):
        status_code = 999
        expected_result = ''
        actual_result = StatusCodes.get_status_message(status_code)
        assert actual_result == expected_result
