class BanklyVisitHTTPException(Exception):
    default_message = "Default HTTP Exception for bankly visit"
    error_code = "UndefinedHTTPError"
    status_code = 400

    def __init__(self, message: str = None, status_code: int = None):
        self.message = message if message else self.default_message
        self.status_code = status_code if status_code else self.status_code


class BanklyVisitException(Exception):
    default_message = "Something went wrong"
    error_code = "ErrorCodeNotDefined"

    def __init__(self, message=None):
        self.message = message if message else self.default_message
        self.error_code = self.error_code


class NotFoundException(BanklyVisitException):
    message = "Not found"
    error_code = "NotFoundError"


class AuthenticationError(BanklyVisitException):
    default_message = "Wrong login or password"
    error_code = "AuthenticationError"


class AlreadyExistsException(BanklyVisitException):
    message = "Already Exists"
    error_code = "DataAlreadyExistsError"


class DataValidationException(BanklyVisitException):
    default_message = "Data entered incorrectly"
    error_code = "IncorrectDataError"


class TimeIsUpException(BanklyVisitException):
    default_message = "Receiving time up"
    error_code = "TimeIsUpException"


class AccessDeniedException(BanklyVisitException):
    default_message = "Access Denied"
    error_code = "AccessDenied"
