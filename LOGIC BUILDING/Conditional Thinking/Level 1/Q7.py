#Take three numbers and print the largest.

a = int(input("Enter first num :"))
b = int(input("Enter second num :"))
c = int(input("Enter third num :"))

if a>b and a>c:
    print(f"{a} is greatest")
elif b>a and b>c:
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")