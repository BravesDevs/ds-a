from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        N = len(nums)
        L=0

        for R in range(N):
            if (R-L)>k:
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
            
    

sln = Solution()
print(sln.containsNearbyDuplicate([1,2,3,1,2,3],2))
