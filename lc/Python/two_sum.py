nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    for index,number in enumerate(nums):
        if target - number in nums[index+1:]:
            return [nums.index(number), nums.index(target - number)]

print(twoSum(nums, target))