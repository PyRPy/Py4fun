# test code for accountant
import unittest
from accountant import Accountant

class TestAccountant(unittest.TestCase):
    """Tests for the class Accountant."""

    def setUp(self):
        self.acc = Accountant()

    def test_initial_balance(self):
        acc = Accountant() # default
        self.assertEqual(acc.balance, 0)

        acc = Accountant(100) # non-default balance
        self.assertEqual(acc.balance, 100)

    def test_deposit(self):
        self.acc.deposit(100)
        self.assertEqual(self.acc.balance, 100)

        # multiple deposits
        self.acc.deposit(100)
        self.acc.deposit(100)
        self.assertEqual(self.acc.balance, 300)

    def test_withdrawal(self):
        self.acc.deposit(1000)
        self.acc.withdrawal(100)
        self.assertEqual(self.acc.balance, 900)

unittest.main()
