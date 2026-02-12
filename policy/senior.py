# senior_version.py
from abc import ABC, abstractmethod


class Policy(ABC):

    @abstractmethod
    def can_read(self) -> bool:
        pass

    @abstractmethod
    def can_write(self) -> bool:
        pass

    @abstractmethod
    def can_delete(self) -> bool:
        pass

    @abstractmethod
    def can_suspend(self) -> bool:
        pass


class AdminPolicy(Policy):
    def can_read(self) -> bool:
        return True

    def can_write(self) -> bool:
        return True

    def can_delete(self) -> bool:
        return True

    def can_suspend(self) -> bool:
        return True


class UserPolicy(Policy):
    def can_read(self) -> bool:
        return True

    def can_write(self) -> bool:
        return True

    def can_delete(self) -> bool:
        return False

    def can_suspend(self) -> bool:
        return False


class ReadOnlyPolicy(Policy):
    def can_read(self) -> bool:
        return True

    def can_write(self) -> bool:
        return False

    def can_delete(self) -> bool:
        return False

    def can_suspend(self) -> bool:
        return False


# Можно легко добавить новую роль
class SuperAdminPolicy(AdminPolicy):
    def can_suspend(self) -> bool:
        print("audit: super admin suspended user")
        return True


class Db:
    def __init__(self, policy: Policy):
        self.policy = policy

    def read_db(self):
        print("read:", "success" if self.policy.can_read() else "denied")

    def write_db(self):
        print("write:", "success" if self.policy.can_write() else "denied")

    def delete_db(self):
        print("delete:", "success" if self.policy.can_delete() else "denied")

    def suspend_user(self):
        print("suspend:", "success" if self.policy.can_suspend() else "denied")


# ===== Пример использования =====

if __name__ == "__main__":
    db = Db(AdminPolicy())
    db.read_db()
    db.delete_db()

    print("----")

    db.policy = ReadOnlyPolicy()  # динамическая смена политики
    db.write_db()
