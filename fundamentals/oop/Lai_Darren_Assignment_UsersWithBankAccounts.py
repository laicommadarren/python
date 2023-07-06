class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
    	self.account.deposit(amount)
        print("New Balance:", self.account.balance)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print("New Balance:", self.account.balance)

    def display_user_balance(self):
        print("Current Balance:", self.account.balance)
    

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