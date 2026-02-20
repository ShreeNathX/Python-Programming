num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

if num_1%2 == 0 and num_2%2 == 0:
    print(f'Both {num_1} and {num_2} are even.')
elif num_1%2 != 0 and num_2%2 != 0:
    print(f'Both {num_1} and {num_2} are odd.')
elif num_1%2 == 0 and num_2%2 != 0:
    print(f'{num_1} is even and {num_2} is odd.')
elif num_1&2 != 0 and num_2%2 == 0:
    print(f'Only {num_2} is even and {num_1} is odd.')
else:
    print('Invalid number.')