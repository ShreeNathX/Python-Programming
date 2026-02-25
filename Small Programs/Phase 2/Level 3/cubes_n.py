n = int(input("Enter any number: "))

print(f"The cube from 1 to {n}:")
for i in range(1, n+1):
    print(i ** 3, end=" ")