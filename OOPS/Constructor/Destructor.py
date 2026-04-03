"""
Use __del__
"""

class test:
    def __init__(self):
        print("Constructor called...")

    def __del__(self):
        print("Destructor called...")

t = test()
del t

"""
Output:
Constructor called...
Destructor called...
"""