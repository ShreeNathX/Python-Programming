"""
Using operator (+, -, *, etc) with custom meaning
"""

class Point:
    def __init__(self, x):
        self.x = x
    
    def __add__(self, other):
        return self.x + other.x
    
P1 = Point(10)
P2 = Point(20)
print(P1 + P2)          # 30