class A:
    def __init__(self):
        self.x = 10          # Public
    
a = A()
print(a.x)                   # Allowed to access

"""
Output:
10
"""
        