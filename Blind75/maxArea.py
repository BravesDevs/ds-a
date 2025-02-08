class Solution:
    def maxArea(self, height):
        l,r=0,len(height)-1
        
        waterArea = 0
        
        while l<r:
            waterArea = max(waterArea,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            elif height[r]<height[l]:
                r-=1
            else:
                l+=1
        return waterArea
    
sln = Solution()
print(sln.maxArea([1,1]))