class Account:

    def __init__(self, account_type: str):
        self.account_type = account_type
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.account_type == 'savings' and amount > self.balance:
            raise ValueError(f'You cannot overdraw on a savings account. Current balance: {self.balance}')
        self.balance -= amount

    def get_info(self):
        return f'This is a {self.account_type} account with a balance of ${self.balance}'


# Exercise 3.1
# Create a pytest fixture that:
# - creates a new savings account
# - yields that to the test method using the fixture
# - prints the result of get_info() after the test has run
#   (if you don't know how to print to the console when running
#    a pytest test, use Google ;)
# Use the fixture in a test to demonstrate that it works

# Exercise 3.2
# Use the same fixture in a parameterized test, so that every
# iteration uses the same setup and teardown. Does the fixture
# behave as you would expect?
