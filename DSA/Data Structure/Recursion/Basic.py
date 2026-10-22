def display(string, n):
    if n == 0:
        return 
    print(n, string)
    display(string, n-1)

display("Rahul", 5)