"""
Methods that work with class variable
Use decorator: @classmethod
First parameter: cls
"""

class student:
    college = "Sage"

    def __int__(self, name):
        self.name = name

    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name
    

student.change_college("IIT")
print(student.college)              # IIT