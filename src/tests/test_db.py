import unittest
from service.db import DBService, DoesNotExist, DuplicateEntry


class DBTestCase(unittest.TestCase):
    def setUp(self):
        self.db = DBService()
        self.db.add("sukjun", 19, "sukjun40@naver.com")
        self.db.add("ricepotato", 21, "ricepotato40@gmail.com")

    def tearDown(self):
        pass

    def test_db_get_by_name(self):
        user = self.db.get_by_name("sukjun")
        assert user["age"] == 19

        with self.assertRaises(DoesNotExist):
            self.db.get_by_name("some name")

    def test_db_get_count(self):
        assert self.db.get_count() == 2
        assert self.db.delete_all()
        assert self.db.get_count() == 0

    def test_get_db_get_users(self):
        users = self.db.get_users()
        assert len(users) == 2

    def test_db_add_user(self):
        assert self.db.add("user2", 21, "user@gmail.com")
        with self.assertRaises(DuplicateEntry):
            self.db.add("sukjun", "44", "sukjun@gmail.com")

    def test_db_delete(self):
        assert self.db.delete_by_name("sukjun")
        with self.assertRaises(DoesNotExist):
            self.db.delete_by_name("abcd")
