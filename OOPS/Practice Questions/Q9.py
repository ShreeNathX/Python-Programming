"""
Create abstract class Employee:
abstract method salary()

Create:
    FullTimeEmployee
    PartTimeEmployee
"""

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def salary(self, amount):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def salary(self):
        return self.hours * self.rate


f = FullTimeEmployee(50000)
p = PartTimeEmployee(5, 200)

print(f.salary())   # 50000
print(p.salary())   # 1000