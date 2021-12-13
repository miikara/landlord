import database as db
from entities.unit import Unit
# Might need to import user_repository for functions that use user attributes


class UnitRepository:
    """Unit repository class which manages the database operations for Unit class when user is logged in"""

    def __init__(self, connection):
        self._connection = connection

    def add_unit_to_database(self, unit):
        """Function allows service to add a new unit to database"""
        conn = self._connection
        with conn:
            conn.execute('INSERT INTO units (username, address, location, square_meters, asking_price, purchase_price, unit_date, owned) values (?, ?, ?, ?, ?, ?, ?, ?);',
                         (unit.username, unit.address, unit.location, unit.square_meters, unit.asking_price, unit.purchase_price, unit.unit_date, unit.owned))
            conn.commit()

    def get_all_units(self):
        """Function allows service to get all data stored for all units as a list of tuples"""
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM units;')
            results = list(cursor)
        return results

    def get_users_units(self, user):
        """Function allows service to get all data stored for all units as a list of tuples for a specific user object"""
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM units WHERE username = ?;', (user.username, ))
            results = list(cursor)
        return results

    def sell_unit(self, unit):
        # Id could be added to object later and search with unit's id. Address is considered unique
        """Function sets unit's owned status to False"""
        conn = self._connection
        with conn:
            conn.execute('UPDATE units SET owned = 0 WHERE address = ?;',
                         (unit.address, ))
            conn.commit()

    def acquire_unit(self, unit):
        # Id could be added to object later and search with unit's id. Address is considered unique
        """Function sets unit's owned status to False"""
        conn = self._connection
        with conn:
            conn.execute('UPDATE units SET owned = 1 WHERE address = ?;',
                         (unit.address, ))
            conn.commit()

unit_repository_used = UnitRepository(connection=db.get_connection())