from src.services.status import Status

class TestStatus:

    def test_get_status_code_success(self):
        status_code = 200
        expected_result = {
            'status': '200 OK'
        }
        actual_result = Status.get_status_message(status_code)
        assert actual_result == expected_result

    def test_get_status_code_fail(self):
        status_code = 999
        expected_result = ''
        actual_result = Status.get_status_message(status_code)
        assert actual_result == expected_result
