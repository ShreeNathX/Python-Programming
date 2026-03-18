d = {"a": 1, "b": 2, "c": 3}

d.pop("a")       # Removes key 'a'
print(d)
# Output: {'b': 2, 'c': 3}

d.popitem()      # Removes last inserted item
print(d)
# Output: {'a': 1, 'b': 2}

del d["b"]       # Delete specific
print(d)
# Output: {'a': 1, 'c': 3}

d.clear()        # Empty dictionary
print(d)
# Output: {}


# Note: I performed them separately.