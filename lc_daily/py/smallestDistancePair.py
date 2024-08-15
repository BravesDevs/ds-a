import math


class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        l = 0
        r = len(nums)-1
        difference = math.inf
        res = []
        # Binary Search - On O(N) Sorted List; N = len(nums)
        N = len(nums)
        for i in range(N-1):
            for j in range(i+1, N):
                res.append(abs(nums[i]-nums[j]))
        res.sort()
        return res[k-1]


sln = Solution()
print(sln.smallestDistancePair([62, 100, 4], 2))
