age = int(input("Enter your age: "))

if age >= 18 and age < 101:
    print("You can vote!!!")
elif age > 0 and age < 18:
    print("You cannot vote!!!")
else:
    print("Invaid age!!!")
