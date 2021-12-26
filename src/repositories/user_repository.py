import database as db
from entities.user import User


class UserRepository:
    """User repository class which manages the database operation for User class and has an automatically created connection after initialised
    """

    def __init__(self, connection):
        self._connection = connection

    def create_user_to_database(self, user):
        """Function allows service to create a new user to database using the user object and its attributes username and password
        
        Args: User object

        Returns: The User object
        """
        conn = self._connection
        with conn:
            conn.execute('INSERT INTO users (username, password) values (?, ?);',
                         (user.username, user.password))
            conn.commit()
        return user

    def delete_all_users_from_database(self):
        """Function clears the users table in database of all records"""
        conn = self._connection
        with conn:
            conn.execute('DELETE FROM users;')
            conn.commit()

    def delete_user_from_database(self, user):
        """Function allows service to drop an existing user from database by passing a user object and using its attribute username
        
        Args: User object
        """
        conn = self._connection
        with conn:
            conn.execute('DELETE FROM users WHERE username = ?;',
                         (user.username, ))
            conn.commit()

    def get_user(self, username):
        """Function that retrieves a user object by its username
        
        Args: username

        Return: User object
        """
        conn = self._connection
        with conn:
            results = conn.execute(
                'SELECT * FROM users WHERE username = ?;', (username, )).fetchone()
            if results != None:
                result_username = results[1]
                result_password = results[2]
                result_user = User(result_username, result_password)
            else:
                result_user = None
        return result_user

    def get_password(self, username):
        """Function that retrieves a user object's password when a user exists in the database
        
        Args: username

        Result: password
        
        """
        conn = self._connection
        with conn:
            result_password = conn.execute(
                'SELECT password FROM users WHERE username = ?;', (username, ))
        return result_password.fetchone()[0]


user_repository_used = UserRepository(connection=db.get_connection())
