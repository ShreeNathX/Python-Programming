num = int(input("Enter any number: "))

count = 0
while num > 0:
    rem = num % 10
    num //= 10
    count += 1

print(f'Total count of digits in number is {count}.')