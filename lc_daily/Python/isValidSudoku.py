import numpy as np


class Solution:
    def isValidSudoku(self, board):
        board = np.array(board)

        hashIndices = {
            0: [0, 1, 2],
            1: [3, 4, 5],
            2: [6, 7, 8]
        }

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.' and (board[i][j] in board[i][j+1:] or np.count_nonzero(board[:, j] == board[i][j]) > 1):
                    return False

                indexRow = i//3
                indexCol = j//3

                unique = set()

                for l in hashIndices[indexRow]:
                    for m in hashIndices[indexCol]:
                        if board[l][m] in unique and board[l][m] != '.':
                            return False
                        unique.add(board[l][m])

        return True


sln = Solution()
print(sln.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
