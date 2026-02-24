num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

if num_1 > 0 and num_2 > 0:
    if (num_1 + num_2) < 100:
        print("Yes!!!")
    else:
        print("NO")
else:
    print("Negative number.")