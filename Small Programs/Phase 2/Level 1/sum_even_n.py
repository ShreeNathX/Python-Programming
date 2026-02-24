n = int(input("Enter any number: "))

temp = 0
for _ in range(0, n+1, 2):
    temp += _

print(f"The sum of even numbers til {n} is {temp}.")