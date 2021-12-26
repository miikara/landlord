import database as db
from entities.charge import Charge
import datetime

class ChargeRepository:
    """charge repository class which manages the database operations for charge class when user is logged in"""

    def __init__(self, connection):
        self._connection = connection

    def add_charge_to_database(self, charge):
        """Function allows service to add a new charge to database"""
        conn = self._connection
        with conn:
            conn.execute('INSERT INTO charges (unit_id, start_date, type, amount, due_dom, description, end_date) values (?, ?, ?, ?, ?, ?, ?);',
                         (charge.unit_id, charge.start_date, charge.type, charge.amount, charge.due_dom, charge.description, charge.end_date))
            conn.commit()

    def delete_all_charges_from_database(self):
        conn = self._connection
        with conn:
            conn.execute('DELETE FROM charges;')
            conn.commit()

    def get_units_charges(self, unit):
        """Function allows service to get all data stored for all charges as a list of tuples for a specific unit object based on its unit id"""
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM charges WHERE unit_id = ? ORDER BY start_date DESC;', (unit.unit_id, ))
            results = list(cursor)
        return results

    def get_unit_ids_latest_maintenance_charge_amount(self, unit_id):
        """Function allows service to get the latest recurring maintenance charge amount of a specific unit id as a float"""
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT amount FROM charges WHERE charges.description = "maintenance" AND charges.type = "recurring" AND charges.unit_id = ? ORDER BY start_date DESC LIMIT 1;', (unit_id, ))
            result = cursor.fetchone()
            if result is not None:
                charge_amount = float(result[0])
            else:
                charge_amount = 0.0
        return charge_amount
 
    def get_unit_ids_latest_maintenance_charge_id(self, unit_id):
        """Function allows service to get the latest recurring maintenance charge of a specific unit id as a number"""
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM charges WHERE charges.description = "maintenance" AND charges.type = "recurring" AND charges.unit_id = ? ORDER BY start_date DESC LIMIT 1;', (unit_id, ))
            result = cursor.fetchone()
            if result is not None:
                result_charge_id = result[0]
            else:
                result_charge_id = 0
        return result_charge_id

    def set_charge_id_end_date(self, charge_id, end_date):
        """Function sets charge ids end date to given date"""
        conn = self._connection
        with conn:
            conn.execute('UPDATE charges SET end_date = ? WHERE charge_id = ?;',
                         (end_date, charge_id))
            conn.commit()
 

charge_repository_used = ChargeRepository(connection=db.get_connection())