class Solution:
    def subsetXORSum(self, nums):
        sumTotal = 0

        for num in nums:
            sumTotal |= num
        return sumTotal << (len(nums) - 1)



sln = Solution()
print(sln.subsetXORSum([5, 1, 6]))
