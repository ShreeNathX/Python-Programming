nums = list(map(int, input("Enter any numbers using space: ").split()))

for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j]>nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)