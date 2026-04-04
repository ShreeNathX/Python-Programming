class A:
    def __init__(self):
        self._x = 20         # Protected

a = A()
print(a._x)                 # Allowed but not recommended

"""
Output:
20
"""