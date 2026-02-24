num = int(input("Enter a number: "))

if num < 0:
    print("Negative numbers cannot be perfect squares.")
else:
    root = int(num ** 0.5)

    if root * root == num:
        print("Perfect square")
    else:
        print("Not a perfect square")