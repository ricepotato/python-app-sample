import logging
from typing import Any

log = logging.getLogger(f"myapp.{__name__}")


class DBException(Exception):
    pass


class DuplicateEntry(DBException):
    """ name 중복 오류 """


class DoesNotExist(DBException):
    """ 존재하지 않는 이름 """


class DBService:
    """ database service """

    def __init__(self):
        self.current_id = 0
        self.data = {}

    def add(self, name: str, age: int, email: str) -> int:
        if name in self.data:
            log.warning("user [%s] already exist.", name)
            raise DuplicateEntry()
        self.current_id += 1
        self.data[name] = {
            "id": self.current_id,
            "name": name,
            "age": age,
            "email": email,
        }
        log.info("add user name=%s age=%s", name, age)
        return self.current_id

    def get_by_name(self, name: str) -> dict:
        try:
            return self.data[name]
        except KeyError:
            log.warning("user [%s] does not exist.", name)
            raise DoesNotExist()

    def get_users(self) -> list[dict[str, Any]]:
        return [user for _, user in self.data.items()]

    def get_count(self) -> int:
        return len(self.data)

    def delete_all(self) -> bool:
        self.data = {}
        self.current_id = 0
        return True

    def delete_by_name(self, name: str) -> bool:
        try:
            del self.data[name]
        except KeyError:
            log.warning("user [%s] does not exist.", name)
            raise DoesNotExist()
        return True
