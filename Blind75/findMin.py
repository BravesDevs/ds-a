class Solution:
    def findMin(self, nums):
        res=nums[0]
        l,r=0,len(nums)-1
        
        while l<=r:
            if nums[l]<nums[r]:
                res=min(res,nums[l])
                break
            else:
                mid=(l+r)//2
                if nums[mid]>=nums[l]:
                    l=mid+1
                else:
                    r=mid-1
        return res
                
                
sln=Solution()
print(sln.findMin([3,4,5,1,2]))