"""
1 
2 3
4 5 6
7 8 9 10
"""
num, n = 1, 5

for i in range(1, n):
    for j in range(i):
        print(num, end=" ")
        num+=1
    print()