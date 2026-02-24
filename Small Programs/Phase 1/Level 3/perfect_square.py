num = int(input("Enter number: "))

if num < 0:
    print("Not a perfect square")
else:
    i = 0
    while i * i <= num:
        if i * i == num:
            print("Perfect square")
            break
        i += 1
    else:
        print("Not a perfect square")