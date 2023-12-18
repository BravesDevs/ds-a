import math


class Sol:
    def targetIndices(self, nums, target):
        nums.sort()
        l, h = 0, len(nums)-1
        left = right = -1
        while l <= h:  # For finding the leftmost index of the target element
            m = (l+h) >> 1
            if nums[m] == target:
                left = m
                h = m-1
            elif nums[m] > target:
                h = m-1
            else:
                l = m+1
        l, h = left, len(nums)-1
        while l <= h:  # For finding the rightmost index of the target element
            m = (l+h) >> 1
            if nums[m] == target:
                right = m
                l = m+1
            elif nums[m] > target:
                h = m-1
            else:
                l = m+1
        if left == -1:
            return []
        ans = range(left, right+1)
        return ans


sln = Sol()
print(sln.targetIndices([1, 2, 5, 2, 3], 3))
