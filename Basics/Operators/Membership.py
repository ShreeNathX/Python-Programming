"""
Used for checking whether a value exists within a sequence like list, tuple, string or dictionary.
"""

A = [2, 4, 6, 7, 8]

print(2 in A)       # Return true as 2 is present in A.
print(3 in A)       # Return fasle as 3 is not present in A.

print(3 not in A)   # Return true as 3 is not present in A.
print(2 not in A)   # Return false as 2 is present in A.