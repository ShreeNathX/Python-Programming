num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

if num_1 % num_2 == 0:
    print(f'{num_1} is multiple of {num_2}')
elif num_2 % num_1 == 0:
    print(f'{num_2} is multiple of {num_1}')
else:
    print("Not muliple of each other.")