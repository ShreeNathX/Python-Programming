x = int(input("Enter x-axis: "))
y = int(input("Enter y-axis: "))

if x > 0 and y > 0:
    print("First quadrant.")
elif x < 0 and y > 0:
    print("Second quadrant.")
elif x < 0 and y < 0:
    print("Third quadrant.")
else:
    print("Fourth quadrant.")