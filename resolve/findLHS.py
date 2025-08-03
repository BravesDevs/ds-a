from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        l,r=0,1
        N=len(nums)
        nums.sort()
        res=0

        while r<N:
            minNum=min(nums[l],nums[r])
            maxNum=max(nums[l], nums[r])
            if maxNum-minNum==1:
                res+=1
            if maxNum-minNum>1:
                while maxNum-nums[l]>1:
                    l+=1
                res+=1
            r+=1

        return res


sln = Solution()
print(sln.findLHS([1,3,2,2,5,2,3,7]))