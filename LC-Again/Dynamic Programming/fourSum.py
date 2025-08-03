from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        N = len(nums)
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                    continue
            for j in range(i+1,N):
                l,r=j+1,N-1

                while l<r:
                    summ = nums[i]+nums[j]+nums[l]+nums[r]
                    arr = [nums[i],nums[j],nums[l],nums[r]]

                    if summ==target:
                        if arr not in res:
                            res.append(arr)
                        l+=1
                        while l<N and nums[l]==nums[l-1]:
                            l+=1
                    elif summ<target:
                        l+=1
                    else:
                        r-=1
        return res
    
sln = Solution()
print(sln.fourSum([2,2,2,2,2],8))