class Account():

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def __str__(self):
        return f"{self.owner}'s account balance is {self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance or amount < 0:
            return False
        else:
            self.balance -= amount
            return True