import numpy as np


class Solution:
    def maximumHappinessSum(self, happiness, k):
        # Depth first Search
        res = 0
        happiness.sort()
        N = len(happiness)-1

        def dfs(index, turn):
            nonlocal res
            nonlocal N
            if turn == 0 or index < 0 or happiness[index] <= 0:
                return

            happiness[index] -= abs(N-index)
            res += happiness[index] if happiness[index] > 0 else 0
            dfs(index-1, turn-1)

        dfs(len(happiness)-1, k)
        return res


sln = Solution()

print(sln.maximumHappinessSum([7, 50, 3], 3))
