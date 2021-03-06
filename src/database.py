import sqlite3

connection = sqlite3.connect('database.db')


def get_connection():
    return connection


def create_users_table(connection):
    with connection:
        connection.execute(
            'CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, \
            username TEXT UNIQUE, password TEXT);')


def drop_users_table(connection):
    with connection:
        connection.execute('DROP TABLE IF EXISTS users;')


def create_units_table(connection):
    with connection:
        connection.execute(
            'CREATE TABLE IF NOT EXISTS units \
            (unit_id INTEGER PRIMARY KEY, username TEXT, address TEXT \
            , location TEXT, construction_year INTEGER, sewage_year INTEGER \
            , facade_year INTEGER, windows_year INTEGER, elevator_year INTEGER \
            , has_elevator INTEGER, square_meters NUM, floor INTEGER \
            , asking_price NUM, purchase_price NUM, acquired_date TIMESTAMP \
            , sold_date TIMESTAMP, owned INTEGER, \
            FOREIGN KEY (username) REFERENCES users (username));')


def drop_units_table(connection):
    with connection:
        connection.execute('DROP TABLE IF EXISTS units;')


def create_leases_table(connection):
    with connection:
        connection.execute(
            'CREATE TABLE IF NOT EXISTS leases \
            (lease_id INTEGER PRIMARY KEY, unit_id INTEGER \
            , created_time TIMESTAMP, start_date TIMESTAMP, end_date TIMESTAMP \
            , end_date_on_contract TIMESTAMP, tenant TEXT, contract_rent NUM \
            , maximum_annual_rent_increase NUM, rent_due_date INTEGER \
            , deposit NUM, FOREIGN KEY (unit_id) REFERENCES units (unit_id));')


def drop_leases_table(connection):
    with connection:
        connection.execute('DROP TABLE IF EXISTS leases;')


def create_charges_table(connection):
    with connection:
        connection.execute(
            'CREATE TABLE IF NOT EXISTS charges (charge_id INTEGER PRIMARY KEY \
            , unit_id INTEGER, start_date TIMESTAMP, type TEXT, amount NUM \
            , due_dom INTEGER, description TEXT, end_date TIMESTAMP \
            , FOREIGN KEY (unit_id) REFERENCES units (unit_id));')


def drop_charges_table(connection):
    with connection:
        connection.execute('DROP TABLE IF EXISTS charges;')


def create_rents_table(connection):
    with connection:
        connection.execute(
            'CREATE TABLE IF NOT EXISTS rents \
            (rent_id INTEGER PRIMARY KEY, lease_id INTEGER, start_date TIMESTAMP \
            , amount NUM, due_dom INTEGER, end_date TIMESTAMP, \
            FOREIGN KEY (lease_id) REFERENCES leases (lease_id));')


def drop_rents_table(connection):
    with connection:
        connection.execute('DROP TABLE IF EXISTS rents;')
