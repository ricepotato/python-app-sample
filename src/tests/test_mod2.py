import unittest
from mod2 import mod_func


class BasicTestMod2(unittest.TestCase):
    def test_mod(self):
        res = mod_func()
        assert res
