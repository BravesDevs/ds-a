from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[i] for i in range(0, len(nums), 2))


sln = Solution()

print(sln.arrayPairSum([1,4,3,2]))  # Example input