import math


class Solution:
    def productExceptSelf(self, nums):
        prods = [1]
        res = []
        cache={}
        while len(nums):
            num = nums.pop(0)
            if num in cache:
                res.append(cache[num])
            else:
                product = math.prod(nums)*math.prod(prods)
                res.append(product)
                cache[num]=product
            prods.append(num)
        return res


sln = Solution()
print(sln.productExceptSelf([-1, 1, 0, -3, 3]))
