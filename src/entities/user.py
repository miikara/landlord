class User:
    """Class representing the user of the landlord service application
    Attributes:
    username of the user, unique username chosen by the user in the signup process
    password of the user, chosen by the user in the signup process
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return str(self.username)
