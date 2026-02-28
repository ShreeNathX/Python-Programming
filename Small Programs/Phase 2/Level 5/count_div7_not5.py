count = 0
for i in range(1, 501):
    if i % 7 == 0 and i % 5 != 0:
        count += 1

print(f'The count of number from 1 to 500 which is divisible by 7 but not 5 are {count}.')