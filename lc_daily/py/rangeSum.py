class Solution:
    def rangeSum(self, nums, left, right):
        N = len(nums)
        POW = (10**9)+7
        rangeSum = []
        for l in range(N):
            for r in range(l+1, N+1):
                rangeSum.append(sum(nums[l:r]))
        rangeSum.sort()
        return sum(rangeSum[left-1:right]) % POW


sln = Solution()
print(sln.rangeSum([1, 2, 3, 4], 1, 5))
