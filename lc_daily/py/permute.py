class Solution:
    def permute(self, nums):
        res = []

        def backtrack(nums, path):
            if not nums:
                res.append(path)
                return

            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], path + [nums[i]])

        backtrack(nums, [])
        return res


sln = Solution()

result = sln.permute([1, 2, 3])

print("Result: ", result)
