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


def create_leases_table(connection):
    with connection:
        connection.execute(
            'CREATE TABLE IF NOT EXISTS leases (lease_id INTEGER PRIMARY KEY, unit_id INTEGER, created_time TIMESTAMP, start_date TIMESTAMP, end_date TIMESTAMP, end_date_on_contract TIMESTAMP, tenant TEXT, contract_rent NUM, maximum_annual_rent_increase NUM, rent_due_date INTEGER, deposit NUM,FOREIGN KEY (unit_id) REFERENCES units (unit_id));')


def drop_leases_table(connection):
    with connection:
        connection.execute('DROP TABLE IF EXISTS leases;')


def create_charges_table(connection):
    with connection:
        connection.execute(
            'CREATE TABLE IF NOT EXISTS charges (charge_id INTEGER PRIMARY KEY, unit_id INTEGER, start_date TIMESTAMP, type TEXT, amount NUM, due_dom INTEGER, description TEXT, end_date TIMESTAMP, FOREIGN KEY (unit_id) REFERENCES units (unit_id));')


def drop_charges_table(connection):
    with connection:
        connection.execute('DROP TABLE IF EXISTS charges;')