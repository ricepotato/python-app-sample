import os
import logging

log = logging.getLogger(f"myapp.{__name__}")


class SomeClass:
    def __init__(self):
        pass

    def add(self, a, b):
        log.info("add %s + %s = %s", a, b, a + b)
        return a + b

    def get_storage_password(self):
        return os.environ["STORAGE_PASSWORD"]
