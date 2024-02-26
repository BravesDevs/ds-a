class Solution:
    def findMin(self, nums):
        l = 0
        r = len(nums)-1
        res = 0

        while l <= r:
            mid = (l+r)//2
            res = nums[mid]
            if nums[mid] >= nums[l]:
                l += 1
            else:
                r -= 1

        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l+r)//2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                r -= 1
            else:
                l += 1

        return res


sln = Solution()

print(sln.findMin([11, 13, 15, 17]))
