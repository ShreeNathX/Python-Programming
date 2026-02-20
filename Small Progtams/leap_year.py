year = int(input("Enter year: "))

if year%4 == 0 and (year%100 != 0 or year%400 == 0):
    print(f'Yes, {year} is leap year.')
else:
    print(f'No, {year} is not leap year.')