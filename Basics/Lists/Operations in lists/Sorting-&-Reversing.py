nums = [3, 1, 4, 2]
a = nums.copy()
b = nums.copy()
c = nums.copy()

a.sort()                        # Sort in ascending order
b.sort(reverse=True)            # Sort in descending order
c.reverse()                     # Reverse the current order

print(a)                 
print(b)                    
print(c)              

