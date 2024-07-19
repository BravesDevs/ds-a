import numpy as np


class Solution:
    def luckyNumbers(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        res = []
        matrix = np.array(matrix)

        for i in range(ROWS):
            if i < m and i < n and min(matrix[i]) == max(list(matrix[:, i])):
                res.append(min(matrix[i]))
        return res


sln = Solution()
print(sln.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
