n = int(input("Enter the number: "))

for i in range(1, n+1):
    fac = 1
    for j in range(1, i+1):
        fac *= j
    print(f'Factorial of {i} is {fac}')
