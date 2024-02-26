import math


class Solution(object):
    def threeSumClosest(self, nums, target):

        summation = 0
        distance = math.inf
        nums.sort()

        for index, element in enumerate(nums):
            if index > 0 and element == nums[index-1]:
                continue
            l, r = index+1, len(nums)-1
            while l < r:
                addition = element+nums[l]+nums[r]
                
                if abs(addition-target) < distance:
                    summation = addition
                    distance = abs(addition-target)

                if addition < target:
                    l += 1
                else:
                    r -= 1

        return summation


sln = Solution()
result = sln.threeSumClosest([-1000,-1000,-1000], 10000)
print("Result: ", result)
