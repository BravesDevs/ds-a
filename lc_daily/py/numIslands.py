from collections import deque


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])

        visit = set()
        res = 0

        def bfs(r, c):
            queue = deque()
            visit.add((r, c))
            queue.append((r, c))
            while queue:
                row, col = queue.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if ((r) in range(ROWS)) and ((c) in range(COLS)) and grid[r][c] == '1' and (r, c) not in visit:
                        visit.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1
        return res
