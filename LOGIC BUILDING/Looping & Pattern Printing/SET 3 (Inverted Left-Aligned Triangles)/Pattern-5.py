"""
Inverted pattern based on user input rows.
"""

n = int(input("Enter the length of rows: "))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i, end="")
    print()