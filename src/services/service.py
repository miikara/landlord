import database
from entities.user import User
from repositories.user_repository import user_repository_used
from entities.unit import Unit
from repositories.unit_repository import UnitRepository

# Database connection for objects requiring it
conn = database.get_connection()
if conn is not None:
    print('Connection established to database from service module')

database.create_users_table(conn)
database.create_units_table(conn)


class LandlordService:
    def __init__(
        self,
        user_repository=user_repository_used
    ):
        self._user = None
        self._user_repository = user_repository

    def create_user(self, chosen_username, chosen_password):
        user_to_create = User(chosen_username, chosen_password)
        user = self._user_repository.create_user_to_database(user_to_create)
        return user_to_create

    def get_user(self, username):
        user = self._user_repository.get_user(username)
        return user

    def get_password(self, username):
        password = self._user_repository.get_password(username)
        return password

    def login(self, username, password):
        user_attempting_login = User(username, password)
        self._user = user_attempting_login
        return user_attempting_login


landlord_service = LandlordService()
