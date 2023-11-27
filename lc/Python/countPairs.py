class Solution:
    def countPairs(self, nums, target):
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] < target:
                    count += 1
        return count


sln = Solution()
print(sln.countPairs([-6, 2, 5, -2, -7, -1, 3], -2))
