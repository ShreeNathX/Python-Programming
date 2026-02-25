num = int(input("Enter any number: "))

result = 0
while num != 0:
    rem = num % 10
    result += rem
    num //= 10

print(f"The sum of digit is: {result}")