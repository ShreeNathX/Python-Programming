for i in range(10, 101):
    num = str(i)
    if (int(num[0]) + int(num[1])) % 3 == 0:
        print(i)