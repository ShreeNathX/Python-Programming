num =  int(input("Enter any number: "))

if num % 5 == 0 and num % 3 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print('Not divisible by both.')