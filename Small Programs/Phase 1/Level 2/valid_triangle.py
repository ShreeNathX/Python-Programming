x = int(input("Enter first side:"))
y = int(input("Enter second side:"))
z = int(input("Enter third side:"))

if x > 0 and y > 0 and z > 0 and (x + y > z and y + z > x and z + x > y):
    print(f'Valid triangle.')
else:
    print(f'Not valid triangle.')