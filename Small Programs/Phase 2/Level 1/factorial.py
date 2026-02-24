n = int(input("Enter any number: "))

fac = 1
if n == 0 or n == 1: 
    print(fac)
elif n > 1:
    for _ in range(n, 0, -1):
        fac *= _
    print(fac)
else:
    print("Invalid number.")