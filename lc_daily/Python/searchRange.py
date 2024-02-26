class Solution(object):
    def searchRange(self, nums, target):

        if target not in nums:
            return [-1, -1]
        if nums.count(target) == 1:
            index = nums.index(target)
            return [index]*2
        l, r = 0, len(nums)-1
        incrLeft, decrRight = True, True

        while incrLeft or decrRight:
            if nums[l] == target:
                incrLeft = False
            if nums[r] == target:
                decrRight = False

            if incrLeft:
                l += 1
            if decrRight:
                r -= 1
        return [l, r]


sln = Solution()
result = sln.searchRange([5, 7, 7, 8, 8, 10], 8)
print("Result: ", result)
