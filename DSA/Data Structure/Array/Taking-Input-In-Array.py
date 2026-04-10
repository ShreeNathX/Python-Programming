n = int(input("Enter the number of array: "))

arr = []
for i in range(n):
    ele = int(input())
    arr.append(ele)

print(arr)

"""
Or 
use map function:
arr = list(map(int, input()))
"""