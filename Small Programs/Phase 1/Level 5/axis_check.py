x = int(input("Enter x-axis: "))
y = int(input("Enter y-axis: "))

if x > 0 and y == 0:
    print("Point lies in x-axis.")
elif y > 0 and x == 0:
    print("Point lies in y-axis")
elif x == 0 and y == 0:
    print("Point lies in origin")
else:
    print("Point doesnot lie in both x-axis and y-axis.")