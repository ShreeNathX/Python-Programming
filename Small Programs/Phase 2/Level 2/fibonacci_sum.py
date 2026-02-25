num = int(input("Enter any number: "))

a = 0
b = 1
temp = 0
for i in range(num):
    c = a + b
    a = b
    b = c
    temp += a

print(f'The sum of fibonacci series is {temp}.')
