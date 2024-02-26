import math


class Sol:
    def targetIndices(self, nums, target):
        nums.sort()
        l = 0
        r = len(nums)-1
        left = right = -1
        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                left = mid
                r = mid-1
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        l, r = left, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                right = mid
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        if left == -1:
            return []

        return range(left, right+1)


sln = Sol()
print(sln.targetIndices([1, 2, 5, 2, 3], 3))
