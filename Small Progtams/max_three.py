nums_1 = float(input("Enter first number: "))
nums_2 = float(input("Enter second number: "))
nums_3 = float(input("Enter third number: "))

if nums_1 > nums_2 and nums_1 > nums_3:
    print(f'{nums_1} is largest.')
elif nums_2 > nums_1 and nums_2 > nums_3:
    print(f'{nums_2} is largest.')
else:
    print(f'{nums_3} is largets.')