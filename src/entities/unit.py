import datetime

class Unit:
    def __init__(self, username, address, location, square_meters=0, asking_price=0, purchase_price=0):
        """
        
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