class Solution:
    def findDuplicate(self, nums):
        nums.sort()

        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r - l) // 2

            if mid > 0 and nums[mid] == nums[mid - 1]:
                return mid
            if nums[mid] > mid:
                l = mid+1
            else:
                r = mid-1
        return -1


sln = Solution()
print(sln.findDuplicate([1, 3, 4, 2, 1]))
