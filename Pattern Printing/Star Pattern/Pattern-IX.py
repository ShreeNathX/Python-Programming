n = 3

for i in range(n):
    print("* " * (n - i) + "  " * (2 * i + 1) + "* " * (n - i))

print()

for i in range(n):
    print("* " * (i + 1) + "  " * (2 * (n - i - 1) + 1) + "* " * (i + 1))