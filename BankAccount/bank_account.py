class BankAccount:
    """
    """
    
    bank_name = "Fisrt National Dojo"
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
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum

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

amy = BankAccount()
brett = BankAccount()

amy.deposit(50).deposit(50).deposit(50).withdrawal(25).yield_interest().display_account_info()
brett.deposit(100).deposit(57).withdrawal(10).withdrawal(10).withdrawal(10).withdrawal(10).yield_interest().display_account_info()

BankAccount.display_all_accounts()