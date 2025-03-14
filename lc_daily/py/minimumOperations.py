from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res=0
        for num in nums:
            if num%3==0:
                continue
            else:
                res = res + 1 if ((num-1)%3==0) or ((num+1)%3==0) else res
        return res
    
sol=Solution()
print(sol.minimumOperations([1,2,3,4])) #3