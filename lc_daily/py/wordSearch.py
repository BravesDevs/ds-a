class Sol:
    def exist(self, matrix, word):
        ROWS, COLS = len(matrix), len(matrix[0])

        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != matrix[r][c] or (r, c) in path:
                return False

            path.add((r, c))

            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i +
                                           1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            path.remove((r, c))

            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True


sln = Sol()

print(sln.exist([["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCCED'))
