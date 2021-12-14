import database as db
from entities.lease import Lease
import datetime

class LeaseRepository:
    """Lease repository class which manages the database operations for Lease class when user is logged in"""

    def __init__(self, connection):
        self._connection = connection

    def add_lease_to_database(self, lease):
        """Function allows service to add a new lease to database"""
        conn = self._connection
        with conn:
            conn.execute('INSERT INTO leases (unit_id, created_time, start_date, end_date, end_date_on_contract, tenant, original_monthly_rent, current_monthly_rent, maximum_annual_rent_increase, rent_due_date, deposit) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);',
                         (lease.unit_id, lease.created_time, lease.start_date, lease.end_date, lease.end_date_on_contract, lease.tenant, lease.original_monthly_rent, lease.current_monthly_rent, lease.maximum_annual_rent_increase, lease.rent_due_date, lease.deposit))
            conn.commit()

    def get_all_leases(self):
        """Function allows service to get all data stored for all leases as a list of tuples"""
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM leases;')
            results = list(cursor)
        return results

    def get_units_leases(self, unit):
        """Function allows service to get all data stored for all leases as a list of tuples for a specific unit object based on its unit id"""
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM leases WHERE unit_id = ? ORDER BY start_date DESC;', (unit.unit_id, ))
            results = list(cursor)
        return results

    def get_users_leases(self, user):
        """Function allows service to get all leases as a list of tuples for a specific user object"""
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM leases INNER JOIN units ON leases.unit_id = units.unit_id WHERE units.username = ?;', (user.username, ))
            results = list(cursor)
        return results

    def set_current_rent(self, lease, new_rent):
        """Function sets lease's current rent to input given with new_rent"""
        conn = self._connection
        with conn:
            conn.execute('UPDATE leases SET current_monthly_rent = ? WHERE lease_id = ?;',
                         (new_rent, lease.lease_id))
            conn.commit()
    
    def end_lease(self, lease):
        """Function sets lease's actual end date to current date"""
        conn = self._connection
        date_to_insert = datetime.datetime.now()
        with conn:
            conn.execute('UPDATE leases SET current_monthly_rent = ? WHERE lease_id = ?;',
                         (date_to_insert, lease.lease_id))
            conn.commit()
 

lease_repository_used = LeaseRepository(connection=db.get_connection())