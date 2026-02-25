num = int(input("Enter any number: "))

result = 0
for _ in range(1, num):
    if num % _ == 0:
        result += _
    
if result == num:
    print("Perfect number.")
else:
    print("Not perfect number.")

