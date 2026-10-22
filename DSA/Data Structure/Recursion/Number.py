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


def nums(n):
    if n == 0:
        return 
    nums(n-1)
    print(n)

nums(10)


"""
Output:
1
2
3
4
5
6
7
8
9
10
"""