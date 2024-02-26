class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid

            # Check if we are in left portion
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            # Check if this is in the right portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid-1
                else:
                    l = mid+1
        return -1


sln = Solution()
print(sln.search([4, 5, 6, 7, 0, 1, 2], 0))
