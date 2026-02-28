for i in range(1, 501):
    original = i
    reverse = 0
    while i > 0:
        rem = i % 10
        reverse = reverse * 10 + rem
        i //= 10
    if original == reverse:
        print(original)
    