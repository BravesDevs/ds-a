class Solution:
    def firstMissingPositive(self, nums):
        nums = set(nums)  # Convert the list to a set for faster membership check

        # Find the first missing positive number
        for i in range(1, len(nums) + 2):
            if i not in nums:
                return i


sln = Solution()
print(sln.firstMissingPositive([1]))
