class Solution:
    def divideArray(self, nums, k):
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            if nums[i+2]-nums[i] > k:
                return []
            res.append(nums[i:i+3])
        return res


sln = Solution()
print(sln.divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2))
