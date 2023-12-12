class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                if sorted(subset.copy()) not in res:
                    res.append(sorted(subset.copy()))
                return

            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        dfs(0)
        return res


sln = Solution()
print(sln.subsets([1, 2, 2]))
