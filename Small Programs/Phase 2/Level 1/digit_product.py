num = int(input("Enter any number: "))

rem = result = 1
while num > 0:
    rem = num % 10
    result *= rem
    num //= 10

print(f'Final product is {result}')

