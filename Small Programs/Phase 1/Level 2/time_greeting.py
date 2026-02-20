time = int(input("Enter current time (0-23): "))

if time >= 4 and time < 12:
    print("Good Morning!!!")
elif time >= 12 and time < 16:
    print("Good Afternoon!!!")
elif time >= 16 and time < 21:
    print("Good Evening!!!")
elif (time >= 21 and time < 24) or (time >= 0 and time < 4):
    print("Good Night!!!")
else:
    print("Invalid Time!!!")


