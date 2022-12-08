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


# Exercise 2.1
# Create a test_data_withdraw object for the withdraw() method
# containing the following test data records:
# balance - amount - new_balance
#    1000 -    100 -         900
#    1000 -    999 -           1
#    1000 -   1000 -           0


# Exercise 2.2
# Create a parametrized test that does the following for each of the
# iterations specified in the test_data_withdraw object:
# 1. Create a new account
#    (the type isn't significant here and can be hard coded to 'savings')
# 2. Make a deposit() to set the initial balance
# 3. Withdraw the given amount
# 4. Check that the actual new balance is equal to the one specified in the test_data object


# Exercise 2.3
# Add a new row to the test_data object with the values
# 1000, 1001 and 1000, respectively. What happens when you run the test again?
# Try to adapt the test so this test case can be run as well. What do you think?
