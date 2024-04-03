import copy


class Solution:
    def exist(self, board, word):
        ROWS = len(board)
        COLS = len(board[0])
        path = set()
        word = list(word)

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0) or (r >= ROWS or c >= COLS) or (word[i] != board[r][c]) or ((r, c) in path):
                return False
            path.add((r, c))
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i +
                                          1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True


sln = Solution()
print(sln.exist([["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
