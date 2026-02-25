char = input("Enter only one character: ").lower()

a_m = "abcdefghijklm"
n_z = "nopqrstuvwxyz"

if len(char) == 1:
    if char in a_m:
        print(f'The range of "{char}" is in between a to m.')
    elif char in n_z:
        print(f'The range of "{char}" is in between n to z.')
    else:
        print(f'{char} is not an alphabet.')
else:
    print("Please provide only one character.")