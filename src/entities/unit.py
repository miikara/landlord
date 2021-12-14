import datetime

class Unit:
    def __init__(self, username, address, location, square_meters=0, asking_price=0, purchase_price=0):
        """
        Class representing a unit acquired by the user

        Attributes:
        username of the units owning user, acting as the foreign key to join to users
        address of the unit, representing the full address of the unit
        location of the unit, representing the area (city or commun) where the unit is located
        square meters of the units, representing the habitable area of the unit
        asking price of the units, representing the original asking price in the listing
        purchase price of the units, representing the final selling price
        unit date, representing the datetime in which the unit object was created in the app
        owned, representing a boolean value that signifies if the unit is still owned (1) or already sold (0)
        """
        self.username = username
        self.address = address
        self.location = location
        self.square_meters = square_meters
        self.asking_price = asking_price
        self.purchase_price = purchase_price
        self.unit_date = datetime.datetime.now()
        self.owned = 1

    def __str__(self):
        return f"Unit owned by {self.username} located at: {self.address}"