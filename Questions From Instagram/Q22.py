a = []
b = []

print(a is b)
print(a == b)

c = 100
d = 100

print(c is d)
print(c == d)

e = int("100")
f = int("100")

print(e is f)
print(e == f)



"""
a is b → False: Lists are two different objects in memory.
a == b → True: Both lists have equal values (empty).
c is d → True: Python typically reuses cached small integers.
c == d → True: Both integers have the same value.
e is f → True (typically): Python caches small integers, including 100, so both may reference the same object.
e == f → True: Both integers have the same value.
"""