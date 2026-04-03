"""
Methods that work with instance variable
"""

class student:
    def __init__(self, name):
        self.name = name
    
    def show(self):                     # Instance Method
        print(self.name)

s1 = student("Ram")
s1.show()