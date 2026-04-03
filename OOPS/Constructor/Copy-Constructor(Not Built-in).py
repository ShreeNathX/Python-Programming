"""
Python doesnot have a built-in copy constructor like c, c++ and other, but we could simulate it.
"""

class student:
    def __init__(self, name):
        self.name = name

    @classmethod
    def copy(cls, other):
        return cls(other.name)

s1 = student("Ram")
s2 = student.copy(s1)

print(s1.name)

"""
Output:
Ram

Alternate Way:
import copy

s2 = copy.copy(s1)       -- Shallow copy
s3 = copy.deepcopy(s1)   -- Deep copy
"""