# Always use get method to fetch value

d = {"name": "Ram", "age": 20}

print(d["city"])       # KeyError
print(d.get("city"))   # None (safe way)

