import numpy as np
import matplotlib.pyplot as plt


class Solution:

    def columnsForEachRow(self, grid):
        checkList = []
        columnizedList = []
        matches = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                checkList.append(grid[j][i])
            columnizedList.append(checkList)
            checkList = []
        for i in columnizedList:
            if i in grid:
                matches += grid.count(i)
        return matches


sln = Solution()
result = sln.columnsForEachRow(
    [[3, 2, 1], [1, 7, 6], [2, 7, 7]])
print(result)
