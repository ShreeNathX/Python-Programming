income = float(input("Enter the income amount: "))
age = int(input("Enter age: "))

if income > 500000 and 18 <= age < 100:
    print("Eligible for tax.")
else:
    print("Not Eligible for tax.")