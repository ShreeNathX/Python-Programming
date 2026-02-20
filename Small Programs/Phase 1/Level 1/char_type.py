char = input("Enter any digit, char, special: ")
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
digit = "1234567890"

if len(char) == 1:
    if char is upper:
        print(f'Uppercase character.')
    elif char is lower:
        print(f'Lowercase character.')
    elif char is digit:
        print(f'Digit.')
    else:
        print(f'Special character.')
else:
    print("Please provide only one character.")