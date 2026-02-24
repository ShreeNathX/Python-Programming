char = input("Enter a character: ")

if len(char) == 1:
    if char.isalpha():
        print("The character is a letter.")
    elif char.isdigit():
        print("The character is digit.")
    else:
        print("The character is neither letter not digit.")
else:
    print("Please enter only one digit.")