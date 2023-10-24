class Solution(object):
    def findDisappearedNumbers(self, nums):
        # Mark the present element
        for n in nums:
            index = abs(n)-1
            nums[index] = -1*abs(nums[index])
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        return res


sln = Solution()
print(sln.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
