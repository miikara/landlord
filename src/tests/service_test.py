import unittest
import database as db
from entities.user import User
from repositories.user_repository import user_repository_used
from repositories.unit_repository import unit_repository_used
from repositories.lease_repository import lease_repository_used
from repositories.charge_repository import charge_repository_used
from repositories.rent_repository import rent_repository_used
from services.service import landlord_service


class TestLandlordService(unittest.TestCase):
    def set_up(self):
        self._user = None
        db.create_users_table(db.get_connetion())
        db.create_units_table(db.get_connetion())

    def test_login(self):
        user_repository_used.delete_all_users_from_database()
        unit_repository_used.delete_all_units_from_database()
        lease_repository_used.delete_all_leases_from_database()
        charge_repository_used.delete_all_charges_from_database()
        rent_repository_used.delete_all_rents_from_database()
        self._user = User('test_username', "test_password")
        user_repository_used.create_user_to_database(self._user)
        landlord_service.login('test_username', 'test_password')
        login_user_username = landlord_service._user.username
        print(login_user_username)
        self.assertEqual(login_user_username, 'test_username')

    if __name__ == "__main__":
        unittest.main()
