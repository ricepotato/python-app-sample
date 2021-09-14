import logging
from service import Services
from service.db import DoesNotExist

log = logging.getLogger(f"myapp.{__name__}")


class MailTask:
    def __init__(self, services: Services):
        """
        Args:
          services: 외부 서비스
        """
        self.services = services

    def send_mail_to_all(self, title: str, content: str) -> int:
        """모든 사용자에게 메일을 보낸다.

        Args:
          title (str): 메일 제목
          content (str): 메일 내용

        Returns:
          메일 보낸 수

        """
        user_list = self.services.db.get_users()
        count = 0
        failed_count = 0
        for user in user_list:
            if self.services.mail.send_mail(user["email"], title, content):
                count += 1
            else:
                failed_count += 1
        log.warning("send sent to %s users. failed %s", count, failed_count)
        return count

    def send_mail_to(self, send_to_name: str, title: str, content: str) -> bool:
        """지정된 사용자에게 메일을 보낸다.

        Args:
          send_to_name (str): 사용자 이름
          title (str): 메일 제목
          content (str): 메일 내용

        Returns:
          메일 보낸 수

        """
        try:
            user = self.services.db.get_by_name(send_to_name)
            return self.services.mail.send_mail(user["email"], title, content)
        except DoesNotExist:
            log.warning("send mail to failed. user not exist.")
            return False
