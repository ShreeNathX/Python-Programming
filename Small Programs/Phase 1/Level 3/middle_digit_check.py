num = int(input("Enter three digit number: "))

# Digit count
string = str(abs(num))
digits = len(string)

if digits > 0 and digits <= 3:
    if string[1] > string[0] and string[1] > string[2]:
        print("Middle digit is largest.")
    elif string[1] < string[0] and string[1] < string[2]:
        print("Middle digit is smallest.")
    else:
        print("Middle digit is neither largest nor smallest.")
else:
    print("Please enter three digit number.")