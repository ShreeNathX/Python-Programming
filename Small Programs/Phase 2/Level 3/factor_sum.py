num = int(input("Enter the number: "))

result = 0
for _ in range(1, num+1):
    if num % _ == 0:
        result += _

print(f'The sum of all factor of the number is {result}.')