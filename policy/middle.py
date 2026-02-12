# middle_version.py
from enum import StrEnum


class Role(StrEnum):
    ADMIN = 'admin'
    USER = 'user'
    RO = 'readonly'


def can_read(role: Role) -> bool:
    return role in [Role.ADMIN, Role.USER, Role.RO]


def can_write(role: Role) -> bool:
    return role in [Role.ADMIN, Role.USER]


def can_delete(role: Role) -> bool:
    return role == Role.ADMIN


def can_suspend(role: Role) -> bool:
    return role == Role.ADMIN


class Db:
    def __init__(self, role: Role):
        self.role = role

    def read_db(self):
        if can_read(self.role):
            print("read: success")
        else:
            print("read: denied")

    def write_db(self):
        if can_write(self.role):
            print("write: success")
        else:
            print("write: denied")

    def delete_db(self):
        if can_delete(self.role):
            print("delete: success")
        else:
            print("delete: denied")

    def suspend_user(self):
        if can_suspend(self.role):
            print("user suspended")
        else:
            print("permission denied")
