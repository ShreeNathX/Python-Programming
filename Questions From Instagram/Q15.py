arr = [1, 5, 2, 3, 4, 5, 1]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    l, r = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    res=[]
    while l and r:
        
        res.append(l.pop(0) if l[0] <r[0] else r.pop(0))
    return res + l + r

nums=merge_sort(arr)

def duplicate(nums):
    i = 0
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return nums[:i + 1]

print(duplicate(nums))
