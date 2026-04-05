"""
Create a class Student with:

attributes: name, marks
method: display details
"""

class Student:
    def stuDetails(self, name, marks):
        self.name = name
        self.marks = marks
    
    def showDetails(self):
        print(f'Name of student is {self.name} and marks is {self.marks}')

s1 = Student()
s1.stuDetails("Harry", 89)
s1.showDetails()

s2 = Student()
s2.stuDetails("Steve", 95)
s2.showDetails()

s3 = Student()
s3.stuDetails("Emma", 86)
s3.showDetails()