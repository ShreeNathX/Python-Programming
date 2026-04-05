"""
Create a class Rectangle:

attributes: length, width
methods:
area()
perimeter()
"""

class Rectangle:
    def area(self, length, width):
        print(f'Area of rectangle is {length * width}')
    
    def perimeter(self, length, width):
        print(f'Perimeter of rectangle is {2 * (length + width)}')

r = Rectangle()
r.area(20, 30)
r.perimeter(20, 30)

"""
output:
Area of rectangle is 600
Perimeter of rectangle is 100
"""