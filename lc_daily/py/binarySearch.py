class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return -1


sln = Solution()
print(sln.search([1, 2, 3, 4, 5, 6, 7], 4))
