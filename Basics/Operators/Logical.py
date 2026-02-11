"""
Used used to evaluate and combine boolean expressions.
"""
x = 5
y = 10

print(f'{x == 5 and y == 10}')      # If both statement are true then it will return true.
print(f'{x == 5 and y == 5}')       # If only one of them is false then it will return false.
print(f'{x == 10 and y == 5}')      # If both statements are false then it will return false.

print(f'{x == 5 or y == 10}')       # If both statement are true then it will return true.
print(f'{x == 5 or y == 5}')        # If one of them is false then also it will return true.
print(f'{x == 10 or y == 15}')      # If both statements are false then it will return false.and

print(f'{not (True)}')              # It just invert the condition. If true and it will return false.
print(f'{not (False)}')             # If false then it will return true.
