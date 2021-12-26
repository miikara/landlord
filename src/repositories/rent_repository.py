import database as db
from entities.rent import Rent
import datetime


class RentRepository:
    """rent repository class which manages the database operations for Rent class"""

    def __init__(self, connection):
        self._connection = connection

    def add_rent_to_database(self, rent):
        """Function allows service to add a new rent to database"""
        conn = self._connection
        with conn:
            conn.execute('INSERT INTO rents (lease_id, start_date, amount, due_dom, end_date) values (?, ?, ?, ?, ?);',
                         (rent.lease_id, rent.start_date, rent.amount, rent.due_dom, rent.end_date))
            conn.commit()

    def delete_all_rents_from_database(self):
        """Function clears the rents table in database of all records"""
        conn = self._connection
        with conn:
            conn.execute('DELETE FROM rents;')
            conn.commit()

    def get_units_rents(self, unit):
        """Function allows service to get all data stored for all rents as a list of tuples for a specific unit object based on its unit id"""
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT rents.rent_id, rents.start_date, rents.amount, rents.due_dom, rents.end_date FROM rents INNER JOIN leases ON rents.lease_id = leases.lease_id WHERE leases.unit_id = ? ORDER BY rents.start_date DESC;', (unit.unit_id, ))
            results = list(cursor)
        return results

    def get_units_latest_rent(self, unit):
        """Function allows service to get the latest rent of a specific unit"""
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT rents.rent_id, rents.start_date, rents.amount, rents.due_dom, rents.end_date FROM rents INNER JOIN leases ON rents.lease_id = leases.lease_id WHERE leases.unit_id = ? ORDER BY rents.start_date DESC LIMIT 1;', (unit.unit_id, ))
            result = cursor.fetchone()
        return result

    def get_unit_ids_latest_rent_id(self, unit_id):
        """Function allows service to get the latest rent id of a specific unit id as a number"""
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT rents.rent_id, rents.start_date, rents.amount, rents.due_dom, rents.end_date FROM rents INNER JOIN leases ON rents.lease_id = leases.lease_id WHERE leases.unit_id = ? ORDER BY rents.start_date DESC LIMIT 1;', (unit_id, ))
            result = cursor.fetchone()
            if result is not None:
                result_rent_id = result[0]
            else:
                result_rent_id = 0
        return result_rent_id

    def get_unit_ids_latest_rent_amount(self, unit_id):
        """Function allows service to get the latest rent amount of a specific unit id as a number"""
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT rents.amount FROM rents INNER JOIN leases ON rents.lease_id = leases.lease_id WHERE leases.unit_id = ? ORDER BY rents.start_date DESC LIMIT 1;', (unit_id, ))
            result = cursor.fetchone()
            if result is not None:
                rent_amount = float(result[0])
            else:
                rent_amount = 0.0
        return rent_amount

    def set_rent_id_end_date(self, rent_id, end_date):
        """Function sets rent ids end date to given date"""
        conn = self._connection
        with conn:
            conn.execute('UPDATE rents SET end_date = ? WHERE rent_id = ?;',
                         (end_date, rent_id))
            conn.commit()


rent_repository_used = RentRepository(connection=db.get_connection())
