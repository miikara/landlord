import database
from entities.user import User
from repositories.user_repository import UserRepository
from entities.unit import Unit
from repositories.unit_repository import UnitRepository

# Database connection for objects requiring it
conn = database.get_connection()
if conn is not None:
    print('Connection established to database from service module')

database.create_users_table(conn)
database.create_units_table(conn)
user_repo_used = UserRepository(conn) # Should these be initialized in repositories themselves?

LoginPrompt = """
-----login menu------
0. Exit application
1. Create account
2. Login to your account
"""

class LandlordService:
    def __init__(
        self,
        user_repository=user_repo_used
    ):
        self._user = None
        self._user_repository = user_repository
    
    # New
    def create_user(self, chosen_username, chosen_password):
        user_to_create = User(chosen_username, chosen_password)
        user = self._user_repository.create_to_database(user_to_create)
        return user

    # Old
    def login(self):
        while True:
            if self._user != None:
                break
            else:
                selected = input(LoginPrompt)
            if selected == '0':
                break
            elif selected == '1':
                username_input = input('Select username: ')
                password_input = input('Select password: ')
                if len(password_input) < 5:
                    print(
                        'Minimum password length is five characters. Please select again.')
                elif self._user_repository.get_user(username_input) is not None:
                    print('Username taken. Please select again.')
                else:
                    user_to_create = User(username_input, password_input)
                    self._user_repository.create_user_to_database(
                        user_to_create)
                    print('User succesfully created.')
            elif selected == '2':
                username_input = input('Username: ')
                password_input = input('Password: ')
                if self._user_repository.get_user(username_input) is not None:
                    password_from_database = self._user_repository.get_password(
                        username_input).fetchone()[0]
                else:
                    password_from_database = ''
                if password_from_database == str(password_input):
                    print('Login succesful')
                    login_user = self._user_repository.get_user(username_input)
                    self._user = login_user
                else:
                    print('Login unsuccesful. Please select again.')
            elif selected == '3':
                username_input = input('Insert username: ')
                retrieved_user = self._user_repository.get_password(
                    username_input)
                # After UI is changed this should return just the user object
                return print(retrieved_user)
            else:
                print('Unknown input, please select again')
        return self._user

landlord_service = LandlordService()
# landlord_service.login() /removed when gui started instead of text ui
conn.close()