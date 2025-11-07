"""
Print a square of any character (e.g. #, $) entered by the user.
"""

a = input("Enter any string: ")
n = int(input("Enter length of square: "))

for i in range(1,n+1):
    for j in range(1, n+1):
        print(a, end="")
    print()