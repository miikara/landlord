import unittest
import database as db
from repositories.user_repository import user_repository_used
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def set_up(self):
        self.user = None
        self.user2 = None
        db.create_users_table(db.get_connetion())

    def test_create_user_to_database(self):
        user_repository_used.delete_all_users_from_database()
        self.user = User('Test_username', 'Test_password')
        user_repository_used.create_user_to_database(self.user)
        result = user_repository_used.get_user('Test_username')
        self.assertNotEqual(result, None)

    def test_delete_user_from_database(self):
        user_repository_used.delete_all_users_from_database()
        self.user = User('Test_username', 'Test_password')
        user_repository_used.create_user_to_database(self.user)
        user_repository_used.delete_user_from_database(self.user)
        result = user_repository_used.get_user('Test_username')
        self.assertEqual(result, None)

    def test_get_user(self):
        user_repository_used.delete_all_users_from_database()
        self.user = User('Test_username', 'Test_password')
        user_repository_used.create_user_to_database(self.user)
        result_user = user_repository_used.get_user('Test_username')
        self.assertNotEqual(result_user, None)

    def test_get_password(self):
        user_repository_used.delete_all_users_from_database()
        self.user = User('Test_username', 'Test_password')
        user_repository_used.create_user_to_database(self.user)
        result_password = user_repository_used.get_password('Test_username')
        self.assertEqual(result_password, 'Test_password')

    if __name__ == "__main__":
        unittest.main()
