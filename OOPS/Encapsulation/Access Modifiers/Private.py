class A:
    def __init__(self):
        self.__x = 20           # Private
    

a = A()
print(a._A__x)                  # Name Mangling

"""
print(a.__x)                    # It will throw error


Note: Name mangling is used to access the private data
    Format:
    _classname__variable

"""