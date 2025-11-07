"""
Inverted alphabet pattern:

ABCDE
ABCD
ABC
AB
A

"""

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(chr(65+j-1),end="")
    print()
