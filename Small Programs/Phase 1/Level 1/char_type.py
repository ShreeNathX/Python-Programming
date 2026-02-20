char = input("Enter any digit, char, special: ")
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

if len(char) == 1:
    if char is upper:
        print(f'Uppercase character.')
    elif char is lower:
        print(f'Lowercase character.')
    else:
        print(f'Special character.')
else:
    print("")