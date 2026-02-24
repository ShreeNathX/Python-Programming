num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))

if (num_1 < num_2 and num_1 > num_3) or (num_1 > num_2 and num_1 < num_3):
    print(f'Median value is {num_1}')
elif (num_2 < num_1 and num_2 > num_3) or (num_2 > num_1 and num_2 < num_3):
    print(f'Median value is {num_2}')
else:
    print(f'Median value is {num_3}')
