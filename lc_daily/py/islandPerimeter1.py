class Solution:
    def islandPerimeter(self, grid):
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        def dfs(i, j):
            nonlocal ROWS, COLS
            if i >= ROWS or j >= COLS or i < 0 or j < 0 or grid[i][j] == 0:
                return 1

            if (i, j) in visit:
                return 0

            visit.add((i, j))

            return dfs(i, j+1)+dfs(i, j-1)+dfs(i+1, j)+dfs(i-1, j)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return dfs(i, j)


sln = Solution()
print(sln.islandPerimeter(
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
