x = 10
def f():
    global x
    x = 20
    print(x)

f()
print(x)

# Output will be 
# 20
# 20