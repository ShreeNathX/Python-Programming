def fuc(*args, **kwargs):
    print(args)
    print(kwargs)

fuc(1, 2, 3, x = 10, y = 30, z = 20)


"""
When we want to add mutliple numbers of arguments then we use args and kwargs:
*args    -- Positional Variable arguments
**kwargs -- Keyword Variable arguments

Output:
(1, 2, 3)
{'x': 10, 'y': 30, 'z': 20}
"""