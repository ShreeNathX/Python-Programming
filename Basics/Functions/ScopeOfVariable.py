"""
Local  -- Defined inside function and accessible only within function
Global -- Defined outside function and accessible anywhere
"""

x = 10          # Global
def fun():
    y = 3       # Local
    print(x + y)

fun()