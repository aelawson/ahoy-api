import pytest

from src.resource.base import BaseResource
from src.utilities.exceptions import MethodNotImplementedException

class TestResource:

    def test_resource_not_implemented(self):
        class ExampleResource(BaseResource):
            def __init__(self):
                super()

        test_resource = ExampleResource()

        with pytest.raises(MethodNotImplementedException):
            test_resource.get()

        with pytest.raises(MethodNotImplementedException):
            test_resource.post()

        with pytest.raises(MethodNotImplementedException):
            test_resource.put()

        with pytest.raises(MethodNotImplementedException):
            test_resource.patch()

        with pytest.raises(MethodNotImplementedException):
            test_resource.delete()
