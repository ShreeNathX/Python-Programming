n = 7

# Upper part
for i in range(1, n + 1, 2):
    print(" " * ((n - i)//2) + "*" * i)

# Lower part
for i in range(n - 2, 0, -2):
    print(" " * ((n - i)//2) + "*" * i)