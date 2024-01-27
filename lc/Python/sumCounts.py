import math


class Solution:
    def sumCounts(self, nums):
        total = 0
        for i in range(1, len(nums) + 1):
            for j in range(len(nums) - i + 1):
                li = nums[j:j+i]
                total += len(set(li))**2
        return total


sln = Solution()

print(sln.sumCounts([2, 2, 5, 5]))
