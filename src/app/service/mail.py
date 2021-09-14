import logging

log = logging.getLogger(f"myapp.{__name__}")


class SendMailService:
    def __init__(self):
        pass

    def send_mail(self, to: str, title: str, content: str) -> bool:
        log.info("send mail to %s [%s]: %s", to, title, content)
        return True
