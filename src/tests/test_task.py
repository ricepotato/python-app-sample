import unittest
from unittest.mock import Mock, call
from service.db import DoesNotExist
from task import MailTask


class MailTaskTestCase(unittest.TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        self.services = Mock()
        self.services.db.get_users = Mock(
            return_value=[
                {"id": 1, "email": "sukjun40@naver.com"},
                {"id": 2, "email": "ricepotato40@gmail.com"},
            ]
        )
        self.task = MailTask(self.services)

    def test_mail_task(self):
        title = "[Notice]"
        content = "hi"
        self.task.send_mail_to_all(title, content)
        self.services.db.get_users.assert_called_once()  # Mock 객체의 property 도 Mock 이 됨
        self.services.mail.send_mail.assert_called()  # send_mail 함수는 1번 이상 호출되어야 함
        self.services.mail.send_mail.assert_has_calls(
            [
                call("sukjun40@naver.com", title, content),
                call("ricepotato40@gmail.com", title, content),
            ]
        )  # send_mail 함수는 두번 호출되고 argument 가 맞아야 함

    def test_mail_task_to_user(self):
        self.services.db.get_by_name = Mock(
            return_value={"id": 1, "email": "sukjun40@naver.com"}
        )
        assert self.task.send_mail_to("sukjun40@.naver.com", "hi", "hello world")

        self.services.db.get_by_name = Mock(
            side_effect=DoesNotExist
        )  # get_by_name 함수에서 DoseNotExist 예외가 발생하게 설정
        assert (
            self.task.send_mail_to("sukjun40@.naver.com", "hi", "hello world") is False
        )  # get_by_name 함수에서 DoesNotExist 예외가 발생하면 send_mail_to 함수가 False return
