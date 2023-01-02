class BankAccount:
    accounts = []
    def __init__(self, int_rate , balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(self.balance)
        return self


    def yield_interest(self):
        if self.balance >= 0:
            self.balance += (self.balance *self.int_rate)
        return self

    @classmethod    
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


##NEW CLASS


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            "Checking Account" : BankAccount(0.01, 100),
            "Savings Account" : BankAccount(.05, 500)
        }
    
    def display_balance(self):
        print(f'Name : {self.name}, Checking Account Balance: ${self.account[ "Checking Account"].display_account_info()}')
        print(f'Name : {self.name}, Savings Account Balance: ${self.account[ "Savings Account"].display_account_info()}')


##OUTPUT CHECK

tara = User("Tara Massan", 'email@address.com')

tara.account["Checking Account"].deposit(100).deposit(100).withdraw(250).yield_interest().display_account_info()
tara.account["Savings Account"].deposit(1000).withdraw(900).yield_interest().display_account_info()

#need to work on 2nd bonus...transfer