class Bank:
    def __init__(self, balance):
        self.__balance = balance            # Private

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Invalid...")
    

b = Bank(1000)
print(b.balance)            # Getter   (Look like variable but calls method)
b.balance = 2000            # Setter
print(b.balance)

"""
Output:
1000
2000

Note: This is modern approach. We use decorator.
@property --> It turns a method into read-only variable
@variable.setter --> It allows you to set value with validation using assignments syntax.
"""
    