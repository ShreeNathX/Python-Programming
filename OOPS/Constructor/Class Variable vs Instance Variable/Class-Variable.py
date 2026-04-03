class student:
    college = "Sage University"

    def __init__(self, name):
        self.name = name
    
s1 = student("Ram")
s2 = student("Sita")

print(f'Student name is {s1.name}. College name is {s1.college}')
print(f'Student name is {s2.name}. College name is {s2.college}')


"""
Output:
Student name is Ram. College name is Sage University
Student name is Sita. College name is Sage University


Note: Declared inside class but outside constructor
"""