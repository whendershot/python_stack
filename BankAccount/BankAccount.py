class BankAccount:
    """
    """
    
    bank_name = "Fisrt National Dojo"
    all_accounts = []
    
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.desposit(balance)
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

    def deposit(self, amount):
        pass

    def withdrawal(self, amount):
        pass

    def display_account_info(self):
        pass

    def yield_interest(self):
        pass