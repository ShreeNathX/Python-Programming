def num(n):
    if n == 0:
        return
    print(n)
    num(n-1)

num(10)

"""
Output:
10
9
8
7
6
5
4
3
2
1
"""