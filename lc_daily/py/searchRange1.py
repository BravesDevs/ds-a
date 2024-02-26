class Solution:
    def searchRange(self, nums, target):

        def binarySearch(nums, target, isLeft):
            l, r = 0, len(nums)-1
            i = -1
            while l <= r:
                mid = (l+r)//2

                if target > nums[mid]:
                    l = mid+1
                elif target < nums[mid]:
                    r = mid-1
                else:
                    i = mid
                    if isLeft:
                        r = mid-1
                    else:
                        l = mid+1

            return i

        return [binarySearch(nums, target, True), binarySearch(nums, target, False)]


sln = Solution()
print(sln.searchRange([5, 7, 7, 8, 8, 10], 8))
