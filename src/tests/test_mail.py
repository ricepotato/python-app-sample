import unittest
from service.mail import SendMailService


class MailServiceTestCase(unittest.TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        self.mail = SendMailService()

    def test_mail_send(self):
        assert self.mail.send_mail("sukjun40@naver.com", "hi", "hello world")
