# Using remove 
nums = [10, 20, 40, 50]
nums.remove(20)                         # Deletes first matching values
print(nums)

# Using pop
nums = [10, 20, 40, 50]
a = nums.copy()
b = nums.copy()
a.pop()                                # Remove last element
b.pop(2)                               # Remove element at index
print(a)
print(b)

# Using del
nums = [30, 'Apple', "b", 40]
del nums[0]                            # Delete element at index
print(nums)

# Using clear
nums = [10, 4, 6, 7, "ap"]
nums.clear()                           # Delete all the elements
print(nums)
