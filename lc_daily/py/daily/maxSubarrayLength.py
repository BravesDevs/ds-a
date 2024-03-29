from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums, k):
        res = 0
        l, r = 0, 0
        freq = defaultdict(int)
        while r < len(nums):
            if freq[nums[r]] < k:
                freq[nums[r]] += 1
                res = max(res, r-l+1)
                r += 1
            else:
                freq[nums[l]] -= 1
                l += 1
        return res


sln = Solution()
print(sln.maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4))
