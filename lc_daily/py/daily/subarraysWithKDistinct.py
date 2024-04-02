from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums, k):
        count = defaultdict(int)
        l_far = 0
        l_near = 0

        for r in range(len(nums)):
            count[nums[r]] += 1

            while len(count) > k:
                count[nums[l_near]] -= 1

            if len(count) == k:
                res += l_near-l_far+1

        return res


sln = Solution()
print(sln.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
