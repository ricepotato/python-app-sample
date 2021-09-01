import logging

from .constants import SOME_VALUE

log = logging.getLogger(f"myapp.{__name__}")


def get_value():
    return SOME_VALUE


def mod_func():
    value = get_value()
    log.info("mod_func... some_value=%s", value)
    return value
