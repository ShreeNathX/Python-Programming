"""
Create:
    Shape class
    Circle, Square subclasses
    Each has area()

--> Call using same function
"""

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

def print_area(Shape):
    print(f'Area is {Shape.area()}')

circle = Circle(5)
square = Square(4)

print_area(circle)
print_area(square)

"""
Output:
Area is 78.5
Area is 16
"""
