class Solution(object):
    def moveZeroes(self, nums):
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums


sln = Solution()
print(sln.moveZeroes([1, 0, 1]))
