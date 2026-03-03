num = input("Enter any number in between 1 to 10000: ")
integer = int(num)
if len(num) >= 1 and len(num) < 10000:
    add, mul = 0, 1
    while integer > 0:
        rem = integer % 10
        add += rem
        mul *= rem
        integer//=10

    if add > mul:
        print("The sum of digits is greater than product of their digits.")
    else:
        print("The sum of digits is smaller than product of their digits.")

else:
    print("Please provide number in between 1-10000.")