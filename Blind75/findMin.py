class Solution:
    def findMin(self, nums):
        l,r=0,len(nums)-1
        res = nums[0]
        
        while l<=r:
            if nums[l]<nums[r]:
                return nums[l]
            else:
                mid=(l+r)//2
                res=min(res,nums[mid])
                if nums[mid]>=nums[l]:
                    l=mid+1
                else:
                    r=mid-1
        return res
    
sln = Solution()
print(sln.findMin([3,4,5,1,2]))