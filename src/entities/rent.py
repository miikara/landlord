import datetime


class Rent:
    def __init__(self, lease_id, start_date, amount, due_dom=1, end_date=None):
        """
        Class representing a rent applied on a unit such as recurring maintenance charges levied. First rent of a unit is created with the lease but changes can be made later due to rent increases

        Attributes:
        lease id of the lease to which the rent belongs to, acting as the foreign key to join to leases
        start date representing when the rent will start to be active
        amount, representing the amount of the rent
        due_dom, short for due day-of-month representing the day on which the payment is due. Default value is the first of the month.
        end date representing when the rent will not apply any longer
        """
        self.lease_id = lease_id
        self.start_date = start_date
        self.amount = amount
        self.due_dom = due_dom
        self.end_date = end_date
