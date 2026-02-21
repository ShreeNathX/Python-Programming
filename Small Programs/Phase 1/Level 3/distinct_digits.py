num_1 = int(input("Enter first digit: "))
num_2 = int(input("Enter second digit: "))
num_3 = int(input("Enter third digit: "))

if num_1 != num_2 and num_2 != num_3:
    print(f"{num_1}, {num_2} and {num_3} are distinct.")
else:
    print(f'Not distinct.')