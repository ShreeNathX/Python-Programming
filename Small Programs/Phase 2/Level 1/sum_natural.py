n = int(input("Enter any number to find sum until: "))

temp = 0
for _ in range(n+1):
    temp += _

print(f'The sum is {temp}')