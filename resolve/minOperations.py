from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        
        for num in nums:
            if num != k:
                res += 1
        
        return res

sln = Solution()
print([3,9,7],5)