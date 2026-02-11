x = int(input("Enter your age: "))

if x <=0 and x > 101:
    print('Invalid Age!')
elif x >= 18 and x <101:
    print("You can vote!")
else:
    print("You can't vote!")