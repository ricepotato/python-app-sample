import unittest
from common.mod import mod_func
from common.constants import SOME_VALUE


class BasicTestMod(unittest.TestCase):
    def test_mod(self):
        assert mod_func() == SOME_VALUE
