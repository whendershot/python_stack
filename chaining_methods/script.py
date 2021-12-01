class User:
    """
    
    """
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

# Create 3 instances of the User class
amy = User("Amy", "a@a.com")
brett = User("Brett", "b@b.com")
conner = User("Conner", "c@c.com")


# Have the first user make 3 deposits and 1 withdrawal and then display their balance
amy.make_deposit(50).make_deposit(50).make_deposit(50).make_withdrawal(25).display_user_balance()


# Have the second user make 2 deposits and 2 withdrawals and then display their balance
brett.make_deposit(25).make_deposit(25).make_withdrawal(10).make_withdrawal(30).display_user_balance()


# Have the third user make 1 deposits and 3 withdrawals and then display their balance
conner.make_deposit(100).make_withdrawal(33).make_withdrawal(33).make_withdrawal(33).display_user_balance()


# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
amy.transfer_money(conner, 50).display_user_balance()
conner.display_user_balance()