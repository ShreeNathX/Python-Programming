num = int(input('Enter any number: '))

string = str(abs(num))

if num % 7 == 0:
    print(f'{num} is the multiple of 7.')
elif string[-1] == 7:
    print(f'{num} ends with 7.')
else:
    print(f'{num} is neither multiple of 7 nor ends with 7.')
