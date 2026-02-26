"""
Arithematic Progression (AP) = a + (n-1) * d
"""
n = int(input("Enter the nth term: "))
a = int(input("Enter the value of a: "))
d = int(input("Enter the value of d: "))

for i in range(1, n+1):
    print(a + (i - 1) * d)
