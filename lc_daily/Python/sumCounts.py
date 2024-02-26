import math


class Solution:
    def sumCounts(self, nums):
        total = 0
        for i in range(len(nums)):
            for j in range(len(nums) - i):
                li = nums[j:(j+i)+1]
                total += len(set(li))**2
        return total


sln = Solution()

print(sln.sumCounts([2, 2, 5, 5]))
