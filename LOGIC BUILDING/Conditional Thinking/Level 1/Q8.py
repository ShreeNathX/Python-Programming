#Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.

temperature = int(input("Enter temperature in celsius :"))

if temperature < 20:
    print("Cold")
elif 20 <= temperature <= 30:
    print("Warm")
else:
    print("Hot")
