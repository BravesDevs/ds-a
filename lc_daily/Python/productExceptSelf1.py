import math
import copy


class Solution:
    def productExceptSelf(self, nums):
        cache = {}
        res = [1]*len(nums)
        for i in range(len(nums)):
            if cache.get(nums[i]):
                res[i] = cache[nums[i]]
            else:
                li = copy.deepcopy(nums)
                li.pop(i)
                res[i] = math.prod(li)
                cache[nums[i]] = res[i]
        return res


sln = Solution()

print(sln.productExceptSelf([-1, 1, 0, -3, 3]))
