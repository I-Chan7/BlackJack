# user wallet

class Wallet():
    def __init__(self):
        """Initialise balance"""
        self.balance = float(1000)


    def get_balance(self):
        """Return wallet balance"""
        return self.balance


    def add_to_wallet(self, amount):
        """Add amount to balance"""
        self.balance += amount

    def subtract_from_wallet(self, amount):
        """"Subtract amount from balance"""
        self.balance -= amount