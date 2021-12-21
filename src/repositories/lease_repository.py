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
            conn.execute('INSERT INTO leases (unit_id, created_time, start_date, end_date, end_date_on_contract, tenant, contract_rent, maximum_annual_rent_increase, rent_due_date, deposit) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);',
                         (lease.unit_id, lease.created_time, lease.start_date, lease.end_date, lease.end_date_on_contract, lease.tenant, lease.contract_rent, lease.maximum_annual_rent_increase, lease.rent_due_date, lease.deposit))
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

    def get_latest_created_active_lease_id(self, unit_id):
        """Function to get latest active lease_id. Used for creation of the initial rent in the lease creation process.
        
        Args:
            unit_id
        
        Returns:
            Lease_id as an integer."""

        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'WITH lease_data AS (SELECT * FROM leases WHERE end_date IS NULL OR end_date > DATE()) SELECT * FROM lease_data WHERE unit_id = ? AND end_date_on_contract > DATE() ORDER BY lease_id DESC LIMIT 1;', (unit_id, ))
            result = cursor.fetchone()
            lease_id = int(result[0])
        return lease_id

    def get_latest_start_date_active_lease(self, unit_id):
        """Function to get latest active lease. Used for latest tenant information in statistics
        
        Args:
            unit_id
        
        Returns:
            Lease's data as a list"""

        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'WITH lease_data AS (SELECT * FROM leases WHERE end_date IS NULL OR end_date > DATE()) SELECT * FROM lease_data WHERE unit_id = ? AND end_date_on_contract > DATE() ORDER BY start_date DESC LIMIT 1;', (unit_id, ))
            result = cursor.fetchone()
        return result

    def get_users_leases(self, user):
        """Function allows service to get all leases as a list of tuples for a specific user object"""
        conn = self._connection
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM leases INNER JOIN units ON leases.unit_id = units.unit_id WHERE units.username = ?;', (user.username, ))
            results = list(cursor)
        return results
    
    def end_lease(self, lease_id, end_date):
        """Function sets lease id's end date to chosen date. End date on contract remains the same"""
        conn = self._connection
        with conn:
            conn.execute('UPDATE leases SET end_date = ? WHERE lease_id = ?;',
                         (end_date, lease_id))
            conn.commit()
 

lease_repository_used = LeaseRepository(connection=db.get_connection())