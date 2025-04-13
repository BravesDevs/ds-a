from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        res = {}
        N = len(nums)

        for i in range(N):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,N-1
            
            while l<r:
                summ = nums[i]+nums[l]+nums[r]
                res[target-summ]=summ
                if summ>=target:
                    r-=1
                else:
                    l+=1
        return res[min(res.keys(), key=abs)]


sln = Solution()
print(sln.threeSumClosest([-1,2,1,-4],1))