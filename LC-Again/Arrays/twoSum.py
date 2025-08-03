from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countDict = {}
        for i in range(len(nums)):
            if target - nums[i] in countDict:
                return [countDict[target - nums[i]], i]
            countDict[nums[i]]=i

        return []


sln = Solution()
print(sln.twoSum([2,7,11,15],9))