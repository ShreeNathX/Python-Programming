import copy

original = [[1, 2], [3, 4]]

# Shallow copy
shallow = copy.copy(original)

# Deep copy
deep = copy.deepcopy(original)

# Modify nested element
original[0][0] = 99

print("Original:", original)
print("Shallow Copy:", shallow)  # changes (shared inner list)
print("Deep Copy:", deep)        # unchanged (independent copy)
