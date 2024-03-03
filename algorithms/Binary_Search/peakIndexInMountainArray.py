class Solution:
    def peakIndexInMountainArray(self, arr):
        l = 0
        r = len(arr)-1
        res = 0
        while l < r:
            mid = l + (r-l)//2
            if arr[mid] < arr[mid+1]:
                l = mid+1
            else:
                r = mid
        return l


sln = Solution()
print(sln.peakIndexInMountainArray([0, 1, 0]))
