nums = [5, 7, 2, 4, 1]

for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j]>nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums) 