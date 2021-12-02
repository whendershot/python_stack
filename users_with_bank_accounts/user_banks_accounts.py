import uuid

class User:
    """
    """

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}

    def create_account(self, account_id=""):
        if account_id == "":
            account_id = str(uuid.uuid4)
        if account_id not in self.accounts:
            self.accounts[account_id] = BankAccount()
        return self

    def make_deposit(self, amount, account_id):
        account = self.accounts[account_id]
        account.deposit(amount)
        return self

    def make_withdrawal(self, amount, account_id):
        account = self.accounts[account_id]
        account.withdrawal(amount)
        return self

    def display_user_balance(self):
        result = 0
        for id, account in self.accounts.items():
            result += account.balance
        print(f"User: {self.name}, Balance: ${result}")

    def transfer_money(self, other_user, destination_account_id, source_account_id, amount):
        source_account = self.accounts[source_account_id]
        destination_account = other_user.accounts[destination_account_id]
        source_account.withdrawal(amount)
        destination_account.deposit(amount)
        return self

class BankAccount:
    """
    """
    
    bank_name = "First National Dojo"
    all_accounts = []
    
    def __init__(self, int_rate = 0.0, balance = 0):
        self.int_rate = 0.0
        self.balance = 0
        self.set_interest_rate(int_rate)
        self.deposit(balance)
        BankAccount.all_accounts.append(self)

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    @classmethod
    def all_balances(cls):
        result = 0
        for account in cls.all_accounts:
            result += account.balance
        return result

    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

    def set_interest_rate(self, int_rate):
        if int_rate < 0:
            return False
        self.int_rate = int_rate
        return self

    def deposit(self, amount):
        if amount < 0:
            return False
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if (self.balance - amount) < 0:
            return False
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        if self.balance < 0:
            return False
        self.balance += self.balance * self.int_rate
        return self



# Create 3 instances of the User class
amy = User("Amy", "a@a.com")
amy.create_account("1")
brett = User("Brett", "b@b.com")
brett.create_account("1")
conner = User("Conner", "c@c.com")
conner.create_account("1")


# Have the first user make 3 deposits and 1 withdrawal and then display their balance
amy.make_deposit(50, "1").make_deposit(50, "1").make_deposit(50, "1").make_withdrawal(25, "1").display_user_balance()
amy.create_account("2")
amy.make_deposit(50, "2").make_deposit(50, "2").make_deposit(50, "2").make_withdrawal(25, "2").display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
brett.make_deposit(25, "1").make_deposit(25, "1").make_withdrawal(10, "1").make_withdrawal(30, "1").display_user_balance()


# Have the third user make 1 deposits and 3 withdrawals and then display their balance
conner.make_deposit(100, "1").make_withdrawal(33, "1").make_withdrawal(33, "1").make_withdrawal(33, "1").display_user_balance()


# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
amy.transfer_money(conner, "1", "1", 50).display_user_balance()
conner.display_user_balance()