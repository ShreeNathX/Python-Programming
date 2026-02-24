num = int(input("Enter three digit number: "))

# digit count
string = str(abs(num))              # Convert number to string and abs remove symbols
digits = len(string)

if digits <= 3 and digits > 0:
    if string[0] != string[1] != string[2]:
        print('All three digits are distinct.')
    else:
        print('Not distinct.')
else:
    print('Please enter three digit number.')
    