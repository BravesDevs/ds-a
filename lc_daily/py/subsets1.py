class Solution:
    def subsets(self, nums):

        def backtrack(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                backtrack(i+1, path+[nums[i]])

        res = []
        backtrack(0, [])
        return res


sln = Solution()
print(sln.subsets([1, 2, 3]))
