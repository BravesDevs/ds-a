class Solution():
    def thirdMax(self, nums):
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)

        count = 0
        maxNum = max(nums)
        nums.sort(reverse=True)
        for i in nums:
            if i < maxNum and count < 2:
                count += 1
                maxNum = i
        return maxNum

# Another SOL
# class Solution(object):
#     def thirdMax(self, nums):
#         nums = list(set(nums))
#         if len(nums)<3:
#             return max(nums)


#         nums.sort(reverse=True)
#         return nums[2]


sln = Solution()
print(sln.thirdMax([1, 2, 2, 5, 3, 5]))
