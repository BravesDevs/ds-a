class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0
        arr2.sort()
        for i in arr1:
            left, right = 0, len(arr2)-1
            while left <= right:
                mid = (left+right)//2
                if abs(i-arr2[mid]) <= d:
                    count += 1
                    break
                elif i < arr2[mid]:
                    right = mid-1
                else:
                    left = mid+1
        return len(arr1)-count


sln = Solution()
print(sln.findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6))
# [4,5,8]
# [1,8,9,10]
