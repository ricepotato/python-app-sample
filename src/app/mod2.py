import logging

from common.constants import SOME_VALUE

log = logging.getLogger(f"myapp.{__name__}")


def get_value():
    return SOME_VALUE


def mod_func():
    value = get_value()
    return f"mod_func... some_value={value}"
