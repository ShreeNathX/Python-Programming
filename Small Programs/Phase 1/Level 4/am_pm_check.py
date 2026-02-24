hours = int(input("Enter hours in 24-hour time: "))
minutes = int(input("Enter minutes: "))

if 0 <= hours < 24 and 0 <= minutes < 60:
    if hours < 12:
        print("AM")
    else:
        print("PM")
else:
    print("Invalid time")