from collections import Counter


class Solution:
    def minIncrementForUnique(self, nums):
        res = 0
        if not nums:
            return res
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                diff = nums[i-1]-nums[i]+1
                nums[i] += diff
                res += diff
        return res


sln = Solution()
print(sln.minIncrementForUnique([2, 3, 3]))


# 3,3,3,4,5
