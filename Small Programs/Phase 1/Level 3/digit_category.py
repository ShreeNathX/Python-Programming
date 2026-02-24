num = int(input("Enter any number: "))

# Digit count
string = str(abs(num))
digits = len(string)

if digits == 1:
    print('The number is single-digit.')
elif digits == 2:
    print('The number is double-digit.')
elif digits > 2:
    print('The number is multi-digit')
else:
    print('Invalid number.')