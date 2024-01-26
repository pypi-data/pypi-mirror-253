class ApiException(Exception):
    def __init__(self, message, status_code=None, payload=None):
        super().__init__(message)  # Initialize the Exception with the message
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        return rv


class DatabaseConnectionDownException(ApiException):
    def __init__(self, message="Database linked down", status_code=503, payload=None):
        super().__init__(message, status_code, payload)


class RuntimeErrorException(ApiException):
    def __init__(self, message="Runtime Error", status_code=500, payload=None):
        super().__init__(message, status_code, payload)


class InvalidRequestException(ApiException):
    def __init__(
        self,
        message="Invalid Request / Expectation Failed",
        status_code=400,
        payload=None,
    ):
        super().__init__(message, status_code, payload)


class PreconditionFailedException(ApiException):
    def __init__(self, message="Precondition Failed", status_code=412, payload=None):
        super().__init__(message, status_code, payload)


class ResourceDuplicateException(ApiException):
    def __init__(self, message="Duplicate / Conflict", status_code=409, payload=None):
        super().__init__(message, status_code, payload)


class MethodHasNotImplemented(ApiException):
    def __init__(self, message="Not implemented", status_code=405, payload=None):
        super().__init__(message, status_code, payload)


class ResourceNotFoundException(ApiException):
    def __init__(self, message="Resource Not Found", status_code=404, payload=None):
        super().__init__(message, status_code, payload)


class NoContent(ApiException):
    def __init__(self, message="No Content", status_code=204, payload=None):
        super().__init__(message, status_code, payload)
