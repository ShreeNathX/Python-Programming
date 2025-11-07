"""
Hollow Rectangle

Input: rows = 4, cols = 6
Output:

******
*    *
*    *
******

Logic:
Print stars for:
first row (i == 1)
last row (i == rows)
first or last column (j == 1 or j == cols)
Else, print space.

"""

rows = 4
cols = 6

for i in range(1,rows+1):
    for j in range(1, cols+1):
        if (i == 1 or i == rows or j == 1 or j == cols):
            print("*", end="")
        else:
            print(" ", end="")
    print()