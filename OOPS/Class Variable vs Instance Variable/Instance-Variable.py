class student:
    def __init__(self, name):
        self.name = name            # Instance Variable
    
s1 = student("Ram")
s2 = student("Sita")

print(s1.name)
print(s2.name)

"""
Output:
Ram
Sita


Note: Declared inside methods
"""