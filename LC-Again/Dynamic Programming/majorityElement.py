from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        l,r = 0,1
        N = len(nums)
        while r<N:
            if nums[l]==nums[r]:
                return nums[l]
            l+=1
            r+=1
        

sln = Solution()
print(sln.majorityElement([3,2,3]))