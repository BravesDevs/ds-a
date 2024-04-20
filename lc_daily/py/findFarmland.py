import copy


class Solution:
    def findFarmland(self, land):

        ROWS = len(land)
        COLS = len(land[0])
        res = []
        visit = set()

        def dfs(r, c):
            if (r >= ROWS or c >= COLS or (r, c) in visit or land[r][c] == 0):
                return r - 1, c - 1

            visit.add((r, c))
            maxRow, maxCol = r, c

            maxRow, maxCol = max(maxRow, dfs(r + 1, c)
                                 [0]), max(maxCol, dfs(r, c + 1)[1])

            return maxRow, maxCol

        for r in range(ROWS):
            for c in range(COLS):
                if land[r][c] == 1 and (r, c) not in visit:
                    maxRow, maxCol = dfs(r, c)
                    res.append([r, c, maxRow, maxCol])

        return res


sln = Solution()
print(sln.findFarmland([[1, 1], [1, 1]]))
