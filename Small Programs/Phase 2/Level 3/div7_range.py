a = int(input("Enter start point: "))
b = int(input("Enter end point: "))

print(f'The numbers that are divisible by 7 from {a} to {b} are: ')
for i in range(a, b+1):
    if i % 7 == 0:
        print(i, end=" ")
    