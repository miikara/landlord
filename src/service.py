import database
from user import User
from repositories.user_repository import UserRepository
from unit import Unit

# Database connection for objects requiring it
conn = database.get_connection()
if conn != None:
    print('Connection established to database')

database.create_users_table(conn)
database.create_units_table(conn)
user_repo_used = UserRepository(conn)

LoginPrompt = """
-----login menu------
0. Exit application
1. Create account
2. Login to your account
"""

MenuPrompt = """
-----login menu------
0. Log out
"""

class LandlordService:
    def __init__(
        self,
        user_repository = user_repo_used
    ):
        self._user = None
        self._user_repository = user_repository

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
                    print('Minimum password length is five characters. Please select again.')
                elif self._user_repository.get_user(username_input) != None:
                    print('Username taken. Please select again.')
                else:
                    user_to_create = User(username_input, password_input)
                    self._user_repository.create_user_to_database(user_to_create)
                    print('User succesfully created.')
            elif selected == '2':
                username_input = input('Username: ')
                password_input = input('Password: ')
                password_from_database = self._user_repository.get_password(username_input).fetchone()[0]
                if password_from_database == str(password_input):
                    print('Login succesful')
                    login_user = self._user_repository.get_user(username_input)
                    self._user = login_user
                else:
                    print('Login unsuccesful. Please select again.')
            elif selected == '3':
                username_input = input('Insert username: ')
                retrieved_user = self._user_repository.get_password(username_input)
                return print(retrieved_user) # After UI is changed this should return just the user object
            else:
                print('Unknown input, please select again')
        return self._user

    def menu(self):
        while True:
            selected = input(MenuPrompt)
            if selected == '0':
                self._user == None
            else:
                print('Unknown input, please select again')


service = LandlordService()
service.login()
#if service._user == None:
#    service.login()
#else:
#    service.menu()
conn.close()