class Solution:
    def combine(self, n: int, k: int):
        def backtrack(start, path):
            if len(path) == k:
                res.append(path)
                return
            for i in range(start, n+1):
                backtrack(i+1, path+[i])
        res = []
        backtrack(1, [])
        return res


sln = Solution()
print(sln.combine(4, 2))
