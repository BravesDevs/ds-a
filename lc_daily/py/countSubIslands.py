import copy


class Solution:
    def countSubIslands(self, grid1, grid2):
        R = len(grid1)
        C = len(grid1[0])

        visit = [[False for _ in range(C)] for _ in range(R)]

        def dfs(r, c):
            if (r < 0 or c < 0 or r == R or c == C or grid2[r][c] == 0 or visit[r][c]):
                return True

            visit[r][c] = True

            res = grid1[r][c] == 1

            res &= dfs(r + 1, c)
            res &= dfs(r - 1, c)
            res &= dfs(r, c + 1)
            res &= dfs(r, c - 1)

            retur   n res

        count = 0

        for r in range(R):
            for c in range(C):
                if grid2[r][c] and not visit[r][c]:
                    if dfs(r, c):
                        count += 1

        return count


sln = Solution()
print(sln.countSubIslands(
    [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]], [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]))
