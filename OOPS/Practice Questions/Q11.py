"""
---Magic Methods---
Create class Book:
    attributes: name, price
    override:
        __str__
        __add__ (add prices)
"""

class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Book name is {self.name}, price is {self.price}"

    def __add__(self, other):           
        return self.price + other.price                 # We are adding only two book price here


# Creating objects
b1 = Book("Science", 300)
b2 = Book("Maths", 200)

# Using __str__
print(b1)

# Using __add__
print("Total price:", b1 + b2)