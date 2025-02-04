import math
class Solution:
    def maxProduct(self,nums):
        #* Brute Force
        # res=nums[0]
        # for i in range(len(nums)):
        #     product=1
        #     for j in range(i,len(nums)):
        #         product*=nums[j]
        #         res=max(res,product)
        # return res
        
        
        res = max(nums)
        curMin,curMax = 1, 1
        
        for n in nums:
            if n==0:
                curMin,curMax=1, 1
                continue
            temp=curMax*n
            curMax=max(temp, n*curMin, n)
            curMin=min(temp, n*curMin, n)
            res = max(res,curMax)
        return res

    
sln =  Solution()
print(sln.maxProduct([2,3,-2,4]))