class BankAccount:

    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self,deposit):
        self.balance += deposit

    def withdraw(self,withdrawal):
        if withdrawal > self.balance:
            print(f"Insufficient funds, {withdrawal} is not in your account!!! ")
        else:
            self.balance -= withdrawal


acount1 = BankAccount()

acount1.deposit(500)
acount1.withdraw(600)

print(f"Balance is: {acount1.balance}")
