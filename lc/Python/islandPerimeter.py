# Using Bounded Matrix

# import numpy as np


# class Solution(object):
#     def islandPerimeter(self, grid):
#         gridPad = np.pad(grid, pad_width=1, mode='constant', constant_values=0)
#         count = 0
#         for i in range(len(grid)):
#             gridRow = i+1
#             for j in range(len(grid[i])):
#                 gridCol = j+1
#                 if gridPad[gridRow][gridCol] == 1:
#                     if gridPad[gridRow][gridCol-1] == 0:
#                         count += 1
#                     if gridPad[gridRow][gridCol+1] == 0:
#                         count += 1
#                     if gridPad[gridRow-1][gridCol] == 0:
#                         count += 1
#                     if gridPad[gridRow+1][gridCol] == 0:
#                         count += 1
#         return count


# Using DFS

class Solution(object):
    def islandPerimeter(self, grid):
        visited = set()

        def dfs(row, col):
            if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0 or grid[row][col] == 0:
                return 1
            if (row, col) in visited:
                return 0

            visited.add((row, col))

            perim = dfs(row, col-1) + dfs(row, col+1) + \
                dfs(row-1, col) + dfs(row+1, col)

            return perim

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)


sln = Solution()
print(sln.islandPerimeter(
    [[1]]))
