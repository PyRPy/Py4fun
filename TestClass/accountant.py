# test class
class Accountant():
    """Manange a bank account."""

    def __init__(self, balance = 0):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

        
