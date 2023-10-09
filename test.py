import unittest
from main import Account

from gradescope_utils.autograder_utils.decorators import weight

class TestAccounts(unittest.TestCase):

    @weight(6)
    def test_account_initialization(self):
        test_account = Account("Mehdi")
        assert test_account.balance == 0
        assert test_account.owner == "Mehdi"

    @weight(4)
    def test_account_objects_to_string(self):
        test_account = Account("Mehdi")

        assert str(test_account) == "Mehdi's account balance is 0"

        test_account.balance = 5
        assert str(test_account) == "Mehdi's account balance is 5"

        test_account.owner = "David"
        assert str(test_account) == "David's account balance is 5"

    @weight(4)
    def test_account_objects_deposit_positive_amount(self):
        test_account = Account("Mehdi")
        assert test_account.balance == 0

        test_account.deposit(100)
        assert test_account.balance == 100

        test_account.deposit(100)
        assert test_account.balance == 200
    
    @weight(4)
    def test_account_objects_deposit_negative_amount(self):
        test_account = Account("Mehdi")
        assert test_account.balance == 0
        test_account.deposit(-10)
        assert test_account.balance == 0

        test_account.deposit(10)
        test_account.deposit(-10)
        assert test_account.balance == 10

    @weight(4)
    def test_account_objects_withdraw_possible_amount(self):
        test_account = Account("Mehdi")
        assert test_account.balance == 0

        test_account.deposit(100)
        assert test_account.balance == 100

        assert test_account.withdraw(40)
        assert test_account.balance == 60

        assert test_account.withdraw(60)
        assert test_account.balance == 0

    @weight(4)
    def test_account_objects_withdraw_negative_amount(self):
        test_account = Account("Mehdi")
        assert test_account.balance == 0

        test_account.deposit(100)
        assert test_account.balance == 100

        assert not test_account.withdraw(-10)
        assert test_account.balance == 100    

    @weight(4)
    def test_account_objects_withdraw_over_balance_amount(self):
        test_account = Account("Mehdi")
        assert test_account.balance == 0

        test_account.deposit(100)
        assert test_account.balance == 100

        assert not test_account.withdraw(1000)
        assert test_account.balance == 100    

if __name__ == '__main__':
    unittest.main()