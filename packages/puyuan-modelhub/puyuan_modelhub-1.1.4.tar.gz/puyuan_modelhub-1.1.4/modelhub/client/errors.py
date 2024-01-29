class APIConnectionError(Exception):
    """APIConnectionError: Error when connecting to the API"""

    def __init__(self, message: str):
        super().__init__(message)


class AuthenticationError(Exception):
    """AuthenticationError: Error when authentication fails"""

    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message)


class InternalServerError(Exception):
    """InternalServerError: Error when the API returns an internal server error"""

    def __init__(self, message: str):
        super().__init__(message)


class APIRateLimitError(Exception):
    """RateLimitError: Error when the API rate limit is exceeded"""

    def __init__(self, message: str):
        super().__init__(message)
