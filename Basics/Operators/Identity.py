"""
Used for compare object identity (Memory Location)
"""

x = int("123")
y = x
z = int("123")

print(f'{y is x}')      # Return true when they both are in same memory location
print(f'{z is x}')
print(f'{z is not x}')


"""
Rule:

In CPython, small integers (typically -5 to 256) are interned (cached), so identical 
small integer literals may reference the same memory object, causing is to return True.
"""