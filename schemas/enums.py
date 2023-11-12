from enum import Enum


class UserRoleEnum(str, Enum):
    client = "client"
    manager = "manager"
    admin = "admin"
    credit_officer = "credit_officer"
