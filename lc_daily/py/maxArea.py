import math
import copy
class Solution:
    def maxArea(self, height):
        l,r=0,len(height)-1
        res=0
        while l<r:
            res = max(res,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res

sln = Solution()
result = sln.maxArea([1,1])
print("Result: ", result)