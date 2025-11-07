"""
Pyramid with continuous numbers:

    1
   123
  12345
 1234567
123456789

"""

rows = 5

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        print(k, end="")
    print()