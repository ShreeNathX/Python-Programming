num = input("Enter any number at least greater than one digit: ")

if len(num) < 2:
    print("Please provide a two-digit number or greater.")
else:
    digits = [int(d) for d in num]  # convert each character to list of integers
    greatest = max(digits)
    smallest = min(digits)
    print(f'{greatest} is greatest and {smallest} is smallest.')