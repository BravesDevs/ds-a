import numpy as np


class Sol:
    def maxIncreaseKeepingSkyline(self, grid):
        rowMax = {}
        colMax = {}
        grid = np.array(grid)
        for i in range(len(grid)):
            rowMax[i] = max(grid[i])
            colMax[i] = max(grid[:, i])
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                count += min(rowMax[i], colMax[j])-grid[i][j]

        return count


sln = Sol()
print(sln.maxIncreaseKeepingSkyline(
    [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
