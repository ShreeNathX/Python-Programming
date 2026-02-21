num_1 = input("Enter first digit: ")
num_2 = input("Enter second digit: ")
num_3 = input("Enter third digit: ")


if num_1.isdigit() and num_2.isdigit() and num_3.isdigit():
    if len(num_1) == 1 and len(num_2) == 1 and len(num_3) == 1:
        num_1, num_2, num_3 = int(num_1), int(num_2), int(num_3)
        if num_1 != num_2 and num_2 != num_3 and num_1 != num_3:
            print(f"{num_1}, {num_2}, and {num_3} are distinct.")
        else:
            print("Not distinct.")
    else:
        print("Please provide only one digit.")
else:
    print("Invalid input. Please enter digits only.")
