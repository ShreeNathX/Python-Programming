from abc import ABC, abstractmethod

class Shape(ABC):       # Abstract Class
    @abstractmethod     # Abstract Method
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def area(self):
        return 10 * 5
    
    def perimeter(self):
        return 2 * (10 + 5)

r = Rectangle()
print(r.area())
print(r.perimeter())