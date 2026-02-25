n = int(input("Enter any number: "))

print(f"The square from 1 to {n}:")
for i in range(1, n+1):
    print(i * i, end=" ")