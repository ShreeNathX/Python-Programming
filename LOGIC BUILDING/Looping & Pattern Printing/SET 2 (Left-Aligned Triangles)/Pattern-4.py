"""
Print a triangle using letters:

A
AB
ABC
ABCD
ABCDE
"""

for i in range(1,6):
    for j in range(i):
        print(chr(65 + j),end="")   #ASCII Code Used Where Char(65) represent A, Char(66) repesent B and so on.
    print()