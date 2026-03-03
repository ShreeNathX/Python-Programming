num = input("Enter three digits number: ")

if len(num) == 3:
    if int(num[0]) + int(num[2]) == int(num[1]):
        print("Yes, they are equal.")
    else:
        print("No, they are not equal.")
else:
    print("Please enter three digits number.")