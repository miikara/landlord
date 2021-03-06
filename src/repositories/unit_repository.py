import database as db
import datetime
from dateutil.relativedelta import relativedelta
from entities.unit import Unit


class UnitRepository:
    """Unit repository class which manages the database operations for Unit class when user is logged in"""

    def __init__(self, connection):
        self._connection = connection

    def add_unit_to_database(self, unit):
        """Function allows service to add a new unit to database
        
        Args: Unit object
        
        """
        conn = self._connection
        with conn:
            conn.execute('INSERT INTO units (username, address, location, construction_year, sewage_year, facade_year, windows_year, elevator_year, has_elevator, square_meters, floor, asking_price, purchase_price, acquired_date, sold_date, owned) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);',
                         (unit.username, unit.address, unit.location, unit.construction_year, unit.sewage_year, unit.facade_year, unit.windows_year, unit.elevator_year, unit.has_elevator, unit.square_meters, unit.floor, unit.asking_price, unit.purchase_price, unit.acquired_date, unit.sold_date, unit.owned))
            conn.commit()

    def delete_all_units_from_database(self):
        """Function clears the units table in database of all records"""
        conn = self._connection
        with conn:
            conn.execute('DELETE FROM units;')
            conn.commit()

    def get_users_units(self, user):
        """Function allows service to get pre-selected data stored for all units where owned equals True as a list of tuples for a specific user object
        
        Args: User object

        Return: List of lists include unit id, address, location, construction year, square meters, floor and purchase price of the unit
        """
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT unit_id, address, location, construction_year, square_meters, floor, purchase_price FROM units WHERE owned = 1 AND username = ?;', (user.username, ))
            results = list(cursor)
        return results

    def get_unit_count_for_date(self, username, date):
        """Function calculates to amount of held units for a user on a given date for a specific username
        
        Args: username, date

        Return: unit count
        """
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'WITH data AS (SELECT * FROM units WHERE acquired_date <= ? AND  sold_date > ?) SELECT username, COUNT(unit_id) FROM data GROUP BY username HAVING username = ?;', (date, date, username))
            result = cursor.fetchone()
            if result is not None:
                unit_count = result[1]
            else:
                unit_count = 0
        return unit_count

    def get_unit_count_time_series(self, username, end_date=datetime.datetime.today().replace(day=1), months_back=24):
        """Function calculates the count of units the user possesses on the first-of-month for given end date and 24 first-of-month dates before that
        
        Args: username, end_date (default the first of current month), months_back (default 24)

        Return: list of dates and unit counts
        """
        dates = []
        unit_counts = []
        for i in range(0, months_back):
            unit_count = self.get_unit_count_for_date(username, end_date)
            dates.append(end_date)
            unit_counts.append(unit_count)
            end_date = end_date - relativedelta(months=1)
        return dates, unit_counts

    def get_users_unit_ids(self, user):
        """Function allows service to get a list of unit ids for a specific user object
        
        Args: User object

        Return: result list of unit ids
        
        """
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT unit_id FROM units WHERE owned = 1 AND username = ?;', (user.username, ))
            results = list(cursor)
            result_list = [i[0] for i in results]
        return result_list

    def get_users_unit_addresses(self, user):
        """Function allows service to get a list of unit addresses for a specific user object
        
        Args: User object

        Return: result list of addresses
        """
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT unit_id FROM units WHERE owned = 1 AND username = ?;', (user.username, ))
            results = list(cursor)
            result_list = [i[2] for i in results]
        return result_list

    def get_unit_ids_purchase_price(self, unit_id):
        """Function allows service to get the purchase price attribute of a unit object with the passed unit id
        
        Args: unit id

        Return: purchase_price
        
        """
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT purchase_price FROM units WHERE unit_id = ?;', (unit_id, ))
            result = cursor.fetchone()
            purchase_price = float(result[0])
        return purchase_price

    def sell_unit(self, unit_id):
        """Function sets unit's owned status to False
        
        Args: unit id

        """
        conn = self._connection
        with conn:
            conn.execute('UPDATE units SET owned = 0 WHERE unit_id = ?;',
                         (unit_id, ))
            conn.commit()

    def set_sold_date(self, sold_date, unit_id):
        """Function sets unit's sold date to date provided
        
        Args: sold date, unit id
        
        """
        conn = self._connection
        with conn:
            conn.execute('UPDATE units SET sold_date = ? WHERE unit_id = ?;',
                         (sold_date, unit_id))
            conn.commit()


unit_repository_used = UnitRepository(connection=db.get_connection())
