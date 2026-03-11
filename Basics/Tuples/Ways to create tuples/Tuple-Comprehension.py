"""
Tuples don't have a direct comprehension syntax like lists,
but you can use a generator expression inside tuple()
"""

t = tuple(x**2 for x in range(5))
print(t)


"""
Output:
(0, 1, 4, 9, 16)
"""