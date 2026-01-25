"""
n = 5  

*  
* *  
* * *  
* * * *  
"""

n=5

for x in range(n):
    for y in range(x):
        print("*", end=" ")
    print()