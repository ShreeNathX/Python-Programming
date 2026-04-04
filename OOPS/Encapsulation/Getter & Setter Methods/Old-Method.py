class Bank:
    def __init__(self, balance):
        self.__balance = balance            # Private

    def getBalance(self):
        return self.__balance
    
    def setBalance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid Amount...")
    
b = Bank(1000)

print(b.getBalance())               # 1000 --> Getter
b.setBalance(-500)                  # Invalid Amount --> Setter
b.setBalance(2000)                  # Setter

print(b.getBalance())               # 2000


"""
Output:
1000
Invalid Amount...
2000

Note: This is traditional way.
"""