class BankAccount:
    def __init__(self,initial_balance):
        self.balance =initial_balance    #initial amount in account
    def deposit(self, amount):
        if amount > 0:
            self.balance+= amount
            print("Amount deposited successfully")
        else:
            print("Invalid deposit amount")
    def withdraw(self, amount):
        if amount <= 0:
            print("Invald withdrawal amount")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")
    def display_balance(self):
        print("Current Balance:", self.balance)
account = BankAccount(1000)
print(account.balance)
account.deposit(500)
print(account.balance)
account.withdraw(300)
print(account.balance)
account.withdraw(2000)
print(account.balance)