from typing import List


class Solution:
    def findPrefixScore(self,nums: List[int]) -> int:
        maxNum=0
        res=[]
        k=0
        for i in range(len(nums)):
            maxNum=max(maxNum,nums[i])
            s=nums[i]+maxNum
            k+=s
            res.append(k)
        return res
    
sln = Solution()
print(sln.findPrefixScore([1,1,2,4,8,16]))