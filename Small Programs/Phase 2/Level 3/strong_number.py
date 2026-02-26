num = int(input("Enter any number: "))
string = str(num)
result = 0

for ch in string:
    digit = int(ch)
    fac = 1
    for i in range(1, digit + 1):
        fac *= i
    result += fac

if num == result:
    print("Strong number.")
else:
    print("Not strong number.")