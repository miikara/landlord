import sqlite3

connection = sqlite3.connect('database.db')


def create_connection():
    created_connection = sqlite3.connect('database.db')
    return created_connection


def get_connection():
    return connection


def create_users_table(connection):
    with connection:
        connection.execute(
            'CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT);')


def drop_users_table(connection):
    with connection:
        connection.execute('DROP TABLE IF EXISTS users;')


def create_units_table(connection):
    with connection:
        connection.execute(
            'CREATE TABLE IF NOT EXISTS units (unit_id INTEGER PRIMARY KEY, username TEXT, address TEXT, location TEXT, square_meters NUM, asking_price NUM, purchase_price NUM, unit_date TIMESTAMP, owned INTEGER, FOREIGN KEY (username) REFERENCES users (username));')


def drop_units_table(connection):
    with connection:
        connection.execute('DROP TABLE IF EXISTS units;')
