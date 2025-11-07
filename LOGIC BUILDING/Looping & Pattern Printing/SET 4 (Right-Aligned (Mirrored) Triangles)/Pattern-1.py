"""
Right-aligned triangle of stars:

    *
   **
  ***
 ****
*****

"""

n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)


n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= n - i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
