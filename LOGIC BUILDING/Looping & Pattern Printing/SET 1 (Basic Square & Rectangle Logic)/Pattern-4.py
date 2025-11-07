"""
Print a square with numbers instead of stars (like 11111, 22222, etc.).
"""

n = int(input("Enter the length of square: "))

for i in range(1,n+1):
    for j in range(1, n+1):
        print(i, end="")
    print()