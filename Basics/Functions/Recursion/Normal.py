"""
When function call themselves inside a function
"""

def printNumber(n,  end = 10):
    if n > end:
        return
    print(n)
    printNumber(n+1, end)

printNumber(1)
