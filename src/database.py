import sqlite3
from unit import Unit
from user import User

# Add db path to config later
# Separate creation and other database functionality to repositories for each entity
# Use objects for attributes and when user is logged in use attributes 
# Possibly separate connection creation

def connect():
    return sqlite3.connect('database.db')

def create_users_table(connection):
    with connection:
        connection.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT);')

def create_user(connection, username, password):
    with connection:
        connection.execute('INSERT INTO users (username, password) values (?, ?);',(username, password))

def get_all_users(connection):
    with connection:
        return connection.execute('SELECT * FROM users;').fetchall() 

def create_units_table(connection):
    with connection:
        connection.execute('CREATE TABLE IF NOT EXISTS units (unit_id INTEGER PRIMARY KEY, username TEXT, address TEXT, location TEXT, square_meters NUM, asking_price NUM, purchase_price NUM);')

def create_unit(connection, username, address, location, square_meters, asking_price, purchase_price):
    with connection:
        connection.execute('INSERT INTO units (username, address, location, square_meters, asking_price, purchase_price) values (?, ?, ?, ?, ?, ?);',(username, address, location, square_meters, asking_price, purchase_price))

def get_all_units_by_username(connection, username):
    with connection:
        return connection.execute('SELECT * FROM units WHERE username =?;',(username, )).fetchall()