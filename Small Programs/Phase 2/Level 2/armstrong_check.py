num = input("Enter any number: ")

length = len(num)
original = int(num)
result = 0
for _ in range(length):
    digit = int(num[_])
    result += digit ** length

if result == original:
    print("The number is armstrong number.")
else:
    print("The number is not armstrong number.")