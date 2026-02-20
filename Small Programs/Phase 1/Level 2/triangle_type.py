x = int(input("Enter first side: "))
y = int(input("Enter second side: "))
z = int(input("Enter third side: "))

if x > 0 and y > 0 and z > 0:
    if x == y and y == z:
        print("Equilateral triangle.")
    elif x == y or y == z or z == x:
        print("Isosceles triangle.")
    else:
        print("Scalene triangle.")
else:
    print("Not valid triangle.")