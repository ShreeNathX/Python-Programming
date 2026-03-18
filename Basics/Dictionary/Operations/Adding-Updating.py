d = {}

# Add
d["name"] = "Ram"                               # Add the element when empty

# Update
d['name'] = "Hari"                              # Override the element when already exit same key

# Multiple update
d.update({"age": 21, "city": "Bhopal"})          # Add element when not exist and if exits replace element

print(d)

"""
Output:
{'name': 'Ram', 'age': 21, 'city': 'Bhopal'}
"""