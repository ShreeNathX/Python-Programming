"""
(Encapsulation)

Create a class BankAccount:

private attribute: balance
methods:
deposit
withdraw
getter using @property

--> Restrict direct access to balance
"""

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance

    def deposited(self, amount):
        if amount > 0:
            self.__balance  += amount
            print(f'Deposited: {amount}')
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'Withdraw: {amount}')
        else:
            print("Insufficient  balance")
        

b = BankAccount(10000)
print(b.balance)                # Getter

b.deposited(2000)
b.withdraw(1000)
print(b.balance)

"""
10000
Deposited: 2000
Withdraw: 1000
11000
"""
    
