d = {"a": 3, "b": 1, "c": 2}

# Sort by keys
sorted_by_keys = dict(sorted(d.items()))
print(sorted_by_keys)

# Sort by values
sorted_by_values = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_by_values)

"""
Output:
{'a': 3, 'b': 1, 'c': 2}
{'b': 1, 'c': 2, 'a': 3}
"""
