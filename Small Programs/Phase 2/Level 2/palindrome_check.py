num = int(input("Enter any number: "))

original = num
result = 0
while num > 0:
    rem = num % 10
    result = result * 10 + rem
    num //= 10

if original == result:
    print("Yes, it is palindrome.")
else:
    print("No, it is not palindrome.")