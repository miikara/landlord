import datetime


class Charge:
    def __init__(self, unit_id, start_date, amount, type="recurring", due_dom=1, description="maintenance", end_date=None):
        """
        Class representing a charge applied on a unit such as recurring maintenance charges levied

        Attributes:
        unit id of the unit to which the charge belongs to, acting as the foreign key to join to units
        start date representing when the charge will start to be levied
        type, either recurring or not recurring with recurring as default
        amount, representing the amount of the charge levied
        due_dom, short for due day-of-month representing the day on which the payment is due. Default value is the first of the month.
        description representing an optional comment on what the charge is based on. Maintenance is the current default value.
        end date representing when the charge will stop to be levied (next day in the case of a one-off charge)
        """
        self.unit_id = unit_id
        self.start_date = start_date
        self.amount = amount
        self.type = type
        self.due_dom = due_dom
        self.description = description
        self.end_date = end_date
