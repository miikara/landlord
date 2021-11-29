import unittest
import database
from repositories.user_repository import UserRepository
from user import User


class TestUserRepository(unittest.TestCase):
    def test_create_user(self):
        test_conn = database.get_connection()
        test_user_repository = UserRepository(test_conn)
        test_user_to_create = User('test_user_name', 'test_password')
        test_user_repository.create_user_to_database(test_user_to_create)
        result = test_user_repository.get_user('test_name')
        test_user_repository.delete_user_from_database(test_user_to_create)
        test_conn.close()
        self.assertNotEqual(result, None)
