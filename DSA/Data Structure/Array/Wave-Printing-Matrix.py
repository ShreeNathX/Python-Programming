matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

for j in range(cols):
    if j % 2 == 0:
        # top to bottom
        for i in range(rows):
            print(matrix[i][j], end=" ")
    else:
        # bottom to top
        for i in range(rows - 1, -1, -1):
            print(matrix[i][j], end=" ")


"""
Output:
1 4 7 8 5 2 3 6 9 
"""