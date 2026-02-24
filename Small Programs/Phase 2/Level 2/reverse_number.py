num = int(input("Enter any number: "))

result = 0
while num > 0:
    rem = num % 10
    result = result * 10 + rem
    num //= 10

print(f'The reverse number of is {result}.')