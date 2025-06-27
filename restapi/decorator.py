from .api import Api
from .utils import ApiUtils

# Task 1 - Modify the class definition to inherit from the API class.
class BaseApiDecorator(Api):
    # Task 2 - Modify the __init__ method to store the API instance.
    def __init__(self, api: Api):
        self.api = api

    # Task 3 - Add the execute_request method that calls the execute_request method of the API instance.
    def execute_request(self, request_data) -> str:
        return self.api.execute_request(request_data)


class LoggingDecorator(BaseApiDecorator):
    # Task 4 - Modify the __init__ method to pass the API instance to the parent class.
    def __init__(self, api: Api):
        super().__init__(api)

    # Task 5 - Implement the execute_request method to log the request data and response data.
    def execute_request(self, request_data) -> str:
        ApiUtils.log_request(request_data)
        return self.api.execute_request(request_data)



class RateLimitDecorator(BaseApiDecorator):
    # Task 4 - Modify the __init__ method to pass the API instance to the parent class.
    def __init__(self, api: Api):
        super().__init__(api)

    # Task 5 - Implement the execute_request method to log the request data and response data.
    def execute_request(self, request_data) -> str:
        ApiUtils.apply_rate_limit(request_data)
        return self.api.execute_request(request_data)