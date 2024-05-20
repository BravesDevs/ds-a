class Solution:
    def combinationSum(candidates, target):
        def backtrack(start, path, target):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                backtrack(i, path + [candidates[i]], target - candidates[i])
        res = []
        candidates.sort()
        backtrack(0, [], target)
        return res


sln = Solution()

print(sln.combinationSum([2, 3, 6, 7], 7))  # [[7],[2,2,3]]
