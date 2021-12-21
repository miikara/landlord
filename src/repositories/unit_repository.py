import database as db
from entities.unit import Unit

class UnitRepository:
    """Unit repository class which manages the database operations for Unit class when user is logged in"""

    def __init__(self, connection):
        self._connection = connection

    def add_unit_to_database(self, unit):
        """Function allows service to add a new unit to database"""
        conn = self._connection
        with conn:
            conn.execute('INSERT INTO units (username, address, location, construction_year, sewage_year, facade_year, windows_year, elevator_year, has_elevator, square_meters, floor, asking_price, purchase_price, unit_date, owned) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);',
                         (unit.username, unit.address, unit.location, unit.construction_year, unit.sewage_year, unit.facade_year, unit.windows_year, unit.elevator_year, unit.has_elevator, unit.square_meters, unit.floor, unit.asking_price, unit.purchase_price, unit.unit_date, unit.owned))
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
        """Function allows service to get pre-selected data stored for all units as a list of tuples for a specific user object"""
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT unit_id, address, location, construction_year, square_meters, floor, purchase_price FROM units WHERE owned = 1 AND username = ?;', (user.username, ))
            results = list(cursor)
        return results

    def get_unit_ids_purchase_price(self, unit_id):
        """Function allows service to get pre-selected data stored for all units as a list of tuples for a specific user object"""
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT purchase_price FROM units WHERE unit_id = ?;', (unit_id, ))
            result = cursor.fetchone()
            purchase_price = float(result[0])
        return purchase_price

    def sell_unit(self, unit):
        """Function sets unit's owned status to False"""
        conn = self._connection
        with conn:
            conn.execute('UPDATE units SET owned = 0 WHERE address = ?;',
                         (unit.address, ))
            conn.commit()

    def acquire_unit(self, unit):
        """Function sets unit's owned status to True"""
        conn = self._connection
        with conn:
            conn.execute('UPDATE units SET owned = 1 WHERE address = ?;',
                         (unit.address, ))
            conn.commit()

unit_repository_used = UnitRepository(connection=db.get_connection())