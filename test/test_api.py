import pytest

from src.services.api import Api
from src.utilities.exceptions import InvalidRouteFormatException

class TestAPI:

    def test_build_route_pattern_success(self):
        route = '/'
        expected_pattern = '^/$'
        actual_pattern = Api.build_route_pattern(route).pattern
        assert actual_pattern == expected_pattern

        route = '/resources/'
        expected_pattern = '^/resources/$'
        actual_pattern = Api.build_route_pattern(route).pattern
        assert actual_pattern == expected_pattern

        route = '/resources/<resource_id>/'
        expected_pattern = '^/resources/(?:(?<=/)(?:(?P<resource_id>[^<>/])/))?$'
        actual_pattern = Api.build_route_pattern(route).pattern
        assert actual_pattern == expected_pattern

        route = '/resources/<resource_id>/items/<item_id>/'
        expected_pattern = '^/resources/(?:(?<=/)(?:(?P<resource_id>[^<>/])/))items/(?:(?<=/)(?:(?P<item_id>[^<>/])/))?$'
        actual_pattern = Api.build_route_pattern(route).pattern
        assert actual_pattern == expected_pattern

    def test_build_route_pattern_fail(self):
        route ='nodelimiter'
        with pytest.raises(InvalidRouteFormatException):
            Api.build_route_pattern(route)

        route ='resources/'
        with pytest.raises(InvalidRouteFormatException):
            Api.build_route_pattern(route)

        route ='resources/<resource_id>/'
        with pytest.raises(InvalidRouteFormatException):
            Api.build_route_pattern(route)

        route ='resources/<resource_id>/items/'
        with pytest.raises(InvalidRouteFormatException):
            Api.build_route_pattern(route)

        route ='resources/<resource_id>/items/<item_id>/'
        with pytest.raises(InvalidRouteFormatException):
            Api.build_route_pattern(route)

        route ='/resources'
        with pytest.raises(InvalidRouteFormatException):
            Api.build_route_pattern(route)

        route ='/resources/<resource_id>'
        with pytest.raises(InvalidRouteFormatException):
            Api.build_route_pattern(route)

        route ='/resources/<resource_id>/items'
        with pytest.raises(InvalidRouteFormatException):
            Api.build_route_pattern(route)

        route ='/resources/<resource_id>/items/<item_id>'
        with pytest.raises(InvalidRouteFormatException):
            Api.build_route_pattern(route)
            