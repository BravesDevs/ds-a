from collections import Counter
class Solution:
    def threeSum(self,nums):
        nums = sorted(nums)
        res=[]
        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            else:
                l,r=i+1,len(nums)-1
                while l<r:
                    threeSum=nums[i]+nums[l]+nums[r]
                    if threeSum<0:
                        l+=1
                    elif threeSum>0:
                        r-=1
                    else:
                        res.append([nums[i],nums[l],nums[r]])
                        l+=1
                        while nums[l]==nums[l-1] and l<r:
                            l+=1       
        return res
                
                
            
        
        
sln = Solution()
print(sln.threeSum([0,0,0,0]))