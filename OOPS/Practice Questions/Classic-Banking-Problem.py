class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.state = "ACTIVE"
        self.attempts = 0

    def check_state(self):
        if self.state == "BLOCKED":
            print("Account is blocked.")
            return False
        elif self.state == "CLOSED":
            print("Account is closed.")
            return False
        return True

    def verify_pin(self, entered_pin):
        if self.pin == entered_pin:
            self.attempts = 0
            return True
        else:
            self.attempts += 1
            print("Wrong PIN")
            if self.attempts >= 3:
                self.state = "BLOCKED"
                print("Account blocked due to multiple wrong attempts.")
            return False

    def deposit(self, amount):
        if self.check_state():
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount, entered_pin):
        if not self.check_state():
            return
        
        if not self.verify_pin(entered_pin):
            return
        
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")

    def check_balance(self, entered_pin):
        if not self.check_state():
            return
        
        if self.verify_pin(entered_pin):
            print(f"Current balance: {self.balance}")

    def close_account(self, entered_pin):
        if self.verify_pin(entered_pin):
            self.state = "CLOSED"
            print("Account closed successfully.")


acc = BankAccount("Harry", 10000, 1234)

acc.deposit(2000)
acc.check_balance(1234)

acc.withdraw(5000, 1111)   # wrong pin
acc.withdraw(5000, 2222)   # wrong pin
acc.withdraw(5000, 3333)   # blocks account

acc.withdraw(1000, 1234)   # won't work (blocked)

acc.close_account(1234)    # won't work (blocked)