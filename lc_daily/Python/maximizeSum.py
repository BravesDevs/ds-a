class Solution:
    def maximizeSum(self, nums, k):
        num = max(nums)
        maxsum = num
        for i in range(k-1):
            num += 1
            maxsum += num
        return maxsum


sln = Solution()
print(sln.maximizeSum([1, 2, 3, 4, 5], 3))
