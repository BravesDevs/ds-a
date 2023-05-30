class Solution:
    def twoSum(self, nums, target):
        for index,number in enumerate(nums):
            if target - number in nums[index+1:]:
                nums[index]=-99
                return [index, nums.index(target - number)]

sln = Solution()
result = sln.twoSum([3,3], 6)
print("Result: ",result)