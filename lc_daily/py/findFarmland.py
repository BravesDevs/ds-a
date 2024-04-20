import copy


class Solution:
    def findFarmland(self, land):
        ROWS = len(land)
        COLS = len(land[0])
        visit = set()
        res = []

        def dfs(r, c, maxRow, maxCol):
            if (r >= ROWS or c >= COLS) or ((r, c) in visit) or (land[r][c] == 0):
                return maxRow, maxCol
            visit.add((r, c))
            if r + 1 < ROWS and land[r + 1][c] == 1:
                maxRow = max(maxRow, r + 1)
                maxRow, maxCol = dfs(r + 1, c, maxRow, maxCol)

            if c + 1 < COLS and land[r][c + 1] == 1:
                maxCol = max(maxCol, c + 1)
                maxRow, maxCol = dfs(r, c + 1, maxRow, maxCol)
            return maxRow, maxCol

        for r in range(ROWS):
            for c in range(COLS):
                li = []
                if land[r][c] == 1 and (r, c) not in visit:
                    li.append(r)
                    li.append(c)
                    maxR, maxC = dfs(r, c, r, c)
                    li.append(maxR)
                    li.append(maxC)
                    if li not in res:
                        res.append(li)
                visit.add((r, c))
        return res


sln = Solution()
print(sln.findFarmland([[1, 1], [1, 1]]))
