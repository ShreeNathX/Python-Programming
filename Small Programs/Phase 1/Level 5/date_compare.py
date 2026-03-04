d1 = int(input("Enter day of first date: "))
m1 = int(input("Enter month of first date: "))

d2 = int(input("Enter day of second date: "))
m2 = int(input("Enter month of second date: "))

if m1 < m2:
    print("First date comes first in the calendar.")
elif m1 > m2:
    print("Second date comes first in the calendar.")
else:
    if d1 < d2:
        print("First date comes first in the calendar.")
    elif d1 > d2:
        print("Second date comes first in the calendar.")
    else:
        print("Both dates are the same.")