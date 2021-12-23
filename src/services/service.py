import database
from entities.user import User
from entities.unit import Unit
from entities.lease import Lease
from entities.charge import Charge
from entities.rent import Rent
from repositories.user_repository import user_repository_used
from repositories.unit_repository import unit_repository_used
from repositories.lease_repository import lease_repository_used
from repositories.charge_repository import charge_repository_used
from repositories.rent_repository import rent_repository_used

conn = database.get_connection()
if conn is not None:
    print('Connection established to database from service module')

database.create_users_table(conn)
database.create_units_table(conn)
database.create_leases_table(conn)
database.create_charges_table(conn)
database.create_rents_table(conn)

class LandlordService:
    def __init__(
        self,
        user_repository=user_repository_used,
        unit_repository=unit_repository_used,
        lease_repository=lease_repository_used,
        charge_repository=charge_repository_used,
        rent_repository=rent_repository_used
    ):
        self._user = None
        self._user_repository = user_repository
        self._unit_repository = unit_repository
        self._lease_repository = lease_repository
        self._charge_repository = charge_repository
        self._rent_repository = rent_repository

    def create_user(self, chosen_username, chosen_password):
        user_to_create = User(chosen_username, chosen_password)
        self._user_repository.create_user_to_database(user_to_create)
        return user_to_create

    def get_user(self, chosen_username):
        user = self._user_repository.get_user(chosen_username)
        return user

    def get_logged_in_user(self):
        return self._user

    def get_password(self, chosen_username):
        password = self._user_repository.get_password(chosen_username)
        return password

    def create_unit(self, chosen_address, chosen_location, chosen_construction_year, chosen_sewage_year, chosen_facade_year, chosen_windows_year, chosen_elevator_year, chosen_has_elevator, chosen_square_meters, chosen_floor, chosen_asking_price, chosen_purchase_price, chosen_acquired_date):
        username_used = str(self._user)
        unit_to_create = Unit(username_used, chosen_address, chosen_location, chosen_construction_year, chosen_sewage_year, chosen_facade_year, chosen_windows_year, chosen_elevator_year, chosen_has_elevator, chosen_square_meters, chosen_floor, chosen_asking_price, chosen_purchase_price, chosen_acquired_date)
        self._unit_repository.add_unit_to_database(unit_to_create)
        return unit_to_create

    def get_units_owned(self):
        units = self._unit_repository.get_users_units(self._user)
        return units

    def sell_unit(self, chosen_unit_id):
        list_of_units = self._unit_repository.get_users_unit_ids(self._user)
        if int(chosen_unit_id) in list_of_units:
            self._unit_repository.sell_unit(chosen_unit_id)

    def create_lease(self, chosen_unit_id, chosen_start_date, chosen_end_date_on_contract, chosen_tenant, chosen_original_monthly_rent, chosen_maximum_annual_rent_increase, chosen_rent_due_date, chosen_deposit):
        lease_to_create = Lease(chosen_unit_id, chosen_start_date, chosen_end_date_on_contract, chosen_tenant, chosen_original_monthly_rent, chosen_maximum_annual_rent_increase, chosen_rent_due_date, chosen_deposit)
        self._lease_repository.add_lease_to_database(lease_to_create)
        return lease_to_create

    def get_latest_active_lease_tenant(self, chosen_unit_id):
        latest_active_lease = self._lease_repository.get_latest_start_date_active_lease(chosen_unit_id)
        if latest_active_lease is not None:
            tenant_result = latest_active_lease[6]
        else:
            tenant_result = "No tenant"
        return tenant_result

    def end_lease(self, chosen_lease_id, chosen_date):
        self._lease_repository.end_lease(chosen_lease_id, chosen_date)

    def create_maintenance_charge(self, chosen_unit_id, chosen_start_date, chosen_amount, chosen_due_dom):
        """This function creates a charge to database based on a Charge object where type, description and end date are the default values and returns the Charge object"""
        maintenance_charge_to_create = Charge(unit_id=chosen_unit_id, start_date=chosen_start_date, amount=chosen_amount, due_dom=chosen_due_dom)
        self._charge_repository.add_charge_to_database(maintenance_charge_to_create)
        return maintenance_charge_to_create

    def get_latest_maintenance_charge_id(self, chosen_unit_id):
        result_charge_id = self._charge_repository.get_unit_ids_latest_maintenance_charge_id(chosen_unit_id)
        return result_charge_id

    def end_maintenance_charge(self, chosen_charge_id, chosen_date):
        self._charge_repository.set_charge_id_end_date(chosen_charge_id, chosen_date)

    def create_rent(self, chosen_unit_id, chosen_start_date, chosen_amount, chosen_due_dom):
        """This function creates a rent to database based on a Rent object where the end date is None (null in database) and returns the Rent object"""
        chosen_lease_id = self._lease_repository.get_latest_created_active_lease_id(chosen_unit_id)
        rent_to_create = Rent(lease_id=chosen_lease_id, start_date=chosen_start_date, amount=chosen_amount, due_dom=chosen_due_dom)
        self._rent_repository.add_rent_to_database(rent_to_create)
        return rent_to_create

    def get_latest_rent_id(self, chosen_unit_id):
        result_rent_id = self._rent_repository.get_unit_ids_latest_rent_id(chosen_unit_id)
        return result_rent_id

    def end_rent(self, chosen_rent_id, chosen_date):
        self._rent_repository.set_rent_id_end_date(chosen_rent_id, chosen_date)

    def get_noi(self, chosen_unit_id, chosen_months=12):
        annual_rent = self._rent_repository.get_unit_ids_latest_rent_amount(chosen_unit_id) * chosen_months
        annual_charges = self._charge_repository.get_unit_ids_latest_maintenance_charge_amount(chosen_unit_id) * 12
        noi = (annual_rent - annual_charges)
        return noi

    def get_cap_rate(self, chosen_unit_id, chosen_months=12, chosen_purchase_tax_rate=2):
        annual_rent = self._rent_repository.get_unit_ids_latest_rent_amount(chosen_unit_id) * chosen_months
        annual_charges = self._charge_repository.get_unit_ids_latest_maintenance_charge_amount(chosen_unit_id) * 12
        purchase_price = self._unit_repository.get_unit_ids_purchase_price(chosen_unit_id) * (1+chosen_purchase_tax_rate/100)
        cap_rate = (annual_rent - annual_charges) / purchase_price
        return cap_rate

    def get_units_history(self, chosen_username):
        dates, units = self._unit_repository.get_unit_count_time_series(chosen_username)
        return dates, units

    def login(self, username, password):
        user_attempting_login = User(username, password)
        self._user = user_attempting_login
        return user_attempting_login

    def logout(self):
        self._user = None

landlord_service = LandlordService()
