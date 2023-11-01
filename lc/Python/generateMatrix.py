import itertools


class Solution:

    def generateMatrix(self, m, n, elements):
        result = [[-1 for i in range(n)] for i in range(m)]
        seen = [[0 for i in range(n)] for i in range(m)]
        dir_row = [0, 1, 0, -1]
        dir_col = [1, 0, -1, 0]
        dir_ind = 0

        x, y = 0, 0

        for i in range(m*n):

            if i >= len(elements):
                return result

            result[x][y] = elements[i]
            seen[x][y] = True

            cal_row = x + dir_row[dir_ind]
            cal_col = y + dir_col[dir_ind]

            if 0 <= cal_row and cal_row < m and 0 <= cal_col and cal_col < n and not (seen[cal_row][cal_col]):
                x = cal_row
                y = cal_col

            else:
                dir_ind = (dir_ind+1) % 4
                x += dir_row[dir_ind]
                y += dir_col[dir_ind]
        return result


sln = Solution()

print(sln.generateMatrix(3, 5, [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]))
