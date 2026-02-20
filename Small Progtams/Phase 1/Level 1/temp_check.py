temp = int(input("Enter the temperature in celsius: "))

if temp < 15:
    print("Cold")
elif temp > 15 and temp < 30:
    print("Warm")
else:
    print("Hot")