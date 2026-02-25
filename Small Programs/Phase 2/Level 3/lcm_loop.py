a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b
while b != 0:
    rem = a % b
    a = b
    b = rem

lcm = (x * y) // a

print(lcm)