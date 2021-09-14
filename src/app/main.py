import sys
import dotenv
import logging

from common.clsmod import SomeClass
from common.mod import mod_func
from mod2 import mod_func as mod2_func
from service import Services
from task import MailTask

dotenv.load_dotenv()

log = logging.getLogger("myapp")
stream_handler = logging.StreamHandler()
format_str = (
    "[%(levelname)s|%(name)s|%(filename)s:%(lineno)s] %(asctime)s : %(message)s"
)
formatter = logging.Formatter(format_str)
stream_handler.setFormatter(formatter)
log.addHandler(stream_handler)
log.setLevel(logging.INFO)
log = logging.getLogger(f"myapp.{__name__}")


def main():
    log.info("main...")
    res = mod_func()
    log.info(res)
    res = mod2_func()
    log.info(res)

    clsobj = SomeClass()
    res = clsobj.add(3, 4)
    if clsobj.get_storage_password() == "1234":
        log.info("password correct.")
    else:
        log.error("wrong password!")

    log.info(f"clsobj.add res={res}")

    services = Services()
    task = MailTask(services)
    task.send_mail_to_all("hello", "world")

    log.info("It Works!")


if __name__ == "__main__":
    exitcode = main()
    sys.exit(exitcode)
