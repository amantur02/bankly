from exceptions import BanklyHTTPException


def validate_phone_number(phone_number: str = None) -> str:
    if phone_number:
        if len(phone_number) < 9 or not phone_number.isdigit():
            raise BanklyHTTPException("Incorrect number entered")
    return phone_number
