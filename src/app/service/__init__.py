from .db import DBService
from .mail import SendMailService


class Services:
    def __init__(self):
        self._db = DBService()
        self._mail = SendMailService()

    @property
    def db(self):
        return self._db

    @property
    def mail(self):
        return self._mail
