import datetime


class Lease:
    def __init__(self, unit_id, start_date, end_date_on_contract, tenant, contract_rent, maximum_annual_rent_increase, rent_due_date, deposit):
        """
        Class representing a lease contract for a unit between the user and a tenant

        Attributes:
        unit id of the unit to which the lease belongs to, acting as the foreign key to join to units
        created time representing when the lease object was created
        start date representing when the lease contract begins
        end date representing the actual date on which the contract is no longer valid due to termination etc
        end date on contract representing the end date on the contract left empty if the contract is valid until either side terminates it
        tenant representing the name of the tenant
        original monthly rent representing the original rent amount on the contract
        current monthly rent representing the latest rent amount (potentially changed due to annual rent increases and set to original monthly rent when object is initialized)
        maximum annual rent increase representing the maximum percentage for annual rent increase on the lease
        rent due date representing when the rent is supposed to be paid each month
        deposit representing the amount required as a deposit before the tenant can move into the unit
        """
        self.unit_id = unit_id
        self.created_time = datetime.datetime.now()
        self.start_date = start_date
        self.end_date = None
        self.end_date_on_contract = end_date_on_contract
        self.tenant = tenant
        self.contract_rent = contract_rent
        self.maximum_annual_rent_increase = maximum_annual_rent_increase
        self.rent_due_date = rent_due_date
        self.deposit = deposit
