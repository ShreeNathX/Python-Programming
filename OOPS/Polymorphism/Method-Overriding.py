class Employee:
    def calculate_salary(self):
        print("Calculating base salary")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Salary = Monthly fixed salary + bonus")

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        print("Salary = Hours worked * hourly rate")


# Creating objects
emp1 = FullTimeEmployee()
emp2 = PartTimeEmployee()

emp1.calculate_salary()
emp2.calculate_salary()


"""
Output:
Salary = Monthly fixed salary + bonus
Salary = Hours worked * hourly rate

Here, calculate_salary of both FullTimeEmployee and PartTimeEmployee are overriding Employee class value
"""