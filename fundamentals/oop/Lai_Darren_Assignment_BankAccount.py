class BankAccount:
    int_rate = .01
    balance = 0
    def __init__(self, int_rate, balance): 
        self.interest_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self
    def display_account_info(self):
        print("interest rate:", self.interest_rate)
        print("balance:", self.balance)
        return self
    def yield_interest(self):
        self.balance = self.balance * (1 + self.interest_rate)
        return self

darren_account = BankAccount(.03, 20000)
justin_account = BankAccount(.05, 50000)
print(darren_account.deposit(500).deposit(1500).deposit(1500).withdraw(2000).yield_interest().display_account_info())
print(justin_account.deposit(4000).deposit(5000).withdraw(500).withdraw(1000).withdraw(1000).withdraw(1500).yield_interest().display_account_info())

