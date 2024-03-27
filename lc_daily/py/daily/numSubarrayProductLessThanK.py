import math


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        l = 0
        res = 0
        product = 1

        for r in range(0, len(nums)):
            product *= nums[r]
            while l <= r and product >= k:
                product = product//nums[l]
                l += 1
            res += (r-l+1)
        return res


sln = Solution()
print(sln.numSubarrayProductLessThanK([1, 2, 3], 0))
