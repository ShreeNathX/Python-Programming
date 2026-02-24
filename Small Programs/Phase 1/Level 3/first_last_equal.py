num = int(input('Enter four digit number: '))

# Digit count
string = str(abs(num))
digits = len(string)

if digits > 0 and digits <= 4:
    if string[0] == string[3]:
        print("First digit and last digit are equal.")
    else:
        print("First digit and last digit are not equal.")
else:
    print("Please enter four digit number.")