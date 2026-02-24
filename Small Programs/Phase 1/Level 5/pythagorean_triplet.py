a = float(input("Enter length of first side: "))
b = float(input("Enter length of second side: "))
c = float(input("Enter length of third side: "))

if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
    print("Yes, they form pythagorean triplet.")
else:
    print("No, they don't form pythagorean triplet.") 