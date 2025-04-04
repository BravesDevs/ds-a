from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res=0
        nums.sort()

        def binary_search(number,l,r):
            while l<=r:
                mid=(l+r)//2
                if nums[mid]+number>=target:
                    r=mid-1
                else:
                    l=mid+1
            return r
        
        for i in range(len(nums)-1):
            right=binary_search(nums[i],i+1,len(nums)-1)
            res+=right-i
        return res

sln = Solution()
print(sln.countPairs([-6,2,5,-2,-7,-1,3],-2))