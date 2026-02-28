day = int(input("Enter days: "))
month = int(input("Enter month (1-12): "))

days_in_month = {
    1 : 31,
    2 : 28,     # Leaving leap year
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10: 31,
    11: 30,
    12: 31
}

if month in days_in_month:
    if 1 <= day <= days_in_month[month]:
        print("Valid date.")
    else:
        print("Invalid date : day is invalid.")
else:
    print("Invalid date : month is invalid")