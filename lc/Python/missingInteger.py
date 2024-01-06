class Solution:
    def missingInteger(self, nums):
        i, j = 0, 1
        summ = []
        summ.append(nums[i])

        while j < len(nums) and nums[j]-nums[j-1] == 1:
            summ.append(nums[j])
            j += 1
        summ = sum(summ)
        while summ in nums:
            summ += 1
        return summ


sln = Solution()
print(sln.missingInteger([3, 4, 5, 1, 12, 14, 13]))
