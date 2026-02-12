# junior_version.py
from enum import StrEnum


class Role(StrEnum):
    ADMIN = 'admin'
    USER = 'user'
    RO = 'readonly'


class Db:
    def __init__(self, role: Role):
        self.role = role

    def read_db(self):
        if self.role in [Role.ADMIN, Role.USER, Role.RO]:
            print("read: success")
        else:
            print("read: denied")

    def write_db(self):
        if self.role in [Role.ADMIN, Role.USER]:
            print("write: success")
        else:
            print("write: denied")

    def delete_db(self):
        if self.role == Role.ADMIN:
            print("delete: success")
        else:
            print("delete: denied")

    def suspend_user(self):
        if self.role == Role.ADMIN:
            print("user suspended")
        else:
            print("permission denied")
