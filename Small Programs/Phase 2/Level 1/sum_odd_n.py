n = int(input("Enter any number: "))

temp = 0
for _ in range(1, n+1, 2):
    temp += _

print(f'The sum of odd number til {n} is {temp}.')