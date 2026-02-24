amount = int(input("Enter amount: "))

if amount % 100 != 0:
    print("Amount cannot be evenly divided using 2000, 500, and 100 notes.")
else:
    n2000 = amount // 2000
    amount %= 2000

    n500 = amount // 500
    amount %= 500

    n100 = amount // 100

    print("Amount can be divided as:")
    print("2000 notes:", n2000)
    print("500 notes:", n500)
    print("100 notes:", n100)