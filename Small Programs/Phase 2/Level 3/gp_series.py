"""
Geometric Progression (GP) = a * r ^ (n-1)
"""
n = int(input("Enter the nth term: "))
a = int(input("Enter the value of a: "))
r = int(input("Enter the value of r: "))

for i in range(1, n+1):
    print(a * (r **(i-1)))