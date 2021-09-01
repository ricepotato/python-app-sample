import os
import unittest
from common.clsmod import SomeClass


class ModClsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        os.environ["STORAGE_PASSWORD"] = "12345"
        self.obj = SomeClass()

    def test_mod(self):
        res = self.obj.add(1, 2)
        assert res == 3
        self.assertEqual(res, 3)

    def test_mod_cfg(self):
        obj = SomeClass()
        password = obj.get_storage_password()
        assert password == "12345"
