class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        # Simulation method
        visited = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        r, c = rStart, cStart
        steps = 1
        res = []
        i = 0
        while len(res) < (rows*cols):
            dr, dc = directions[i]
            for _ in range(steps):
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
                r, c = r+dr, c+dc
            i = (i+1) % 4
            dr, dc = directions[i]
            for _ in range(steps):
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
                r, c = r+dr, c+dc
            i = (i+1) % 4
            steps += 1
        return res


sln = Solution()
print(sln.spiralMatrixIII(5, 6, 1, 4))
