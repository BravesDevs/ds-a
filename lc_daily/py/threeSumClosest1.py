from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        distance = float('inf')
        N = len(nums)

        for i in range(N):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,N-1
            
            while l<r:
                summ = nums[i]+nums[l]+nums[r]
                if abs(target-summ)<=distance:
                    distance=abs(target-summ)
                    op=summ
                if summ>=target:
                    r-=1
                else:
                    l+=1
        return op


sln = Solution()
print(sln.threeSumClosest([10,20,30,40,50,60,70,80,90],1))