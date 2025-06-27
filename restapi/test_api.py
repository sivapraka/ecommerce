import unittest
from unittest.mock import patch

from .decorator import *
from .api import *


class TestApiDecorator(unittest.TestCase):

    def setUp(self):
        self.api = ECommerceApi()

    def test_has_render_method(self):
        self.assertTrue(
            hasattr(BaseApiDecorator, "execute_request"),
            "If the decorator pattern is implemented correctly, BaseApiDecorator should have a execute_request method.",
        )

    def test_inherits_from_ImageEditor(self):
        self.assertTrue(
            issubclass(BaseApiDecorator, Api),
            "If the decorator pattern is implemented correctly, BaseApiDecorator should inherit from Api.",
        )

    @patch.object(ApiUtils, "log_request", return_value=None)
    def test_log_decorator_execute_request(self, mock_log_request):
        decorator = LoggingDecorator(self.api)
        try:
            decorator.execute_request({"data": "data"})
        except AttributeError as e:
            self.fail(
                "If the decorator pattern is implemented correctly, LoggingDecorator should have a execute_request method."
            )
        mock_log_request.assert_called_once()

    @patch.object(ApiUtils, "apply_rate_limit", return_value=None)
    def test_rate_limit_decorator_execute_request(self, mock_apply_rate_limit):
        decorator = RateLimitDecorator(self.api)
        try:
            decorator.execute_request({"data": "data"})
        except AttributeError as e:
            self.fail(
                "If the decorator pattern is implemented correctly, RateLimitDecorator should have a execute_request method."
            )
        mock_apply_rate_limit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
