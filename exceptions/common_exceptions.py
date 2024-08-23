class RootException(Exception):
    default_message = "Something went wrong"
    error_code = "ErrorCodeNotDefined"

    def __init__(self, message=None, error_field=None):
        self.message = message if message else self.default_message
        self.error_code = self.error_code
        self.error_field = error_field


class NotFoundException(RootException):
    message = "Not found"
    error_code = "NotFoundError"

