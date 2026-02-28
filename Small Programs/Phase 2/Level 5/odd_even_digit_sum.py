num = input("Enter the number (at least two digits): ")

if len(num) < 2:
    print("Enter two digit number or more.")
else:
    odd_sum = even_sum = 0
    for i in range(len(num)):
        if int(num[i]) % 2 == 0:
            even_sum += int(num[i])
        else:
            odd_sum += int(num[i])
    print(f'The sum of odd digits is {odd_sum}.')
    print(f'The sum of even digits is {even_sum}.')