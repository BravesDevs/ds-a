import heapq
from typing import List
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums1 = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(nums1)
        for _ in range(k):
            minValue, index = heapq.heappop(nums1)
            nums[index] = minValue * multiplier
            heapq.heappush(nums1, (nums[index], index))
            
        return nums
    
sol = Solution()
print(sol.getFinalState([2,1,3,5,6], 5, 2)) 