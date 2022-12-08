class Account:

    def __init__(self, account_type: str):
        self.account_type = account_type
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.account_type == 'savings' and amount > self.balance:
            raise ValueError(f'You cannot overdraw on a savings account. Current balance: {self.balance}')

# Exercise 1.1
# Write a test_deposit() method that does the following:
# 1. Create a new Account my_account with account type "savings"
# 2. Deposit 200 to my_account using the deposit() method
# 3. Assert that my_account.balance equals 200

# Exercise 1.2
# Write a test_withdraw() method that does the following:
# 1. Create a new Account my_account with account type "savings"
# 2. Deposit 300 to my_account using the deposit() method
# 2. Withdraw 250 from my_account using the withdraw() method
# 3. Assert that my_account.balance equals 50

# Exercise 1.3
# Create a test method test_withdraw_raises_error()
# that performs the following steps:
# 1. Create a new account of type "savings"
# 2. Deposit 1000 to my_account using the deposit() method
# 2. Try to withdraw 1250 from the account
# 3. Check that a ValueError is raised

# Exercise 1.4
# Extend the previous test so that it also checks the message
# raised by the error, and that the balance is intact (i.e, is still equal to 1000)
