from math import inf


class Solution:
    def maxSubArray(self, nums):
        maxSub = nums[0]
        curSum = 0

        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSub = max(maxSub, curSum)
        return maxSub


sln = Solution()
print(sln.maxSubArray([1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]))
