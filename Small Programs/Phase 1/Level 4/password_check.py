password = input("Enter the password: ")

if len(password) >= 8 and any(digit.isdigit() for digit in password):
    print("Valid Password.")
else:
    print('Invalid Password.')