import itertools


class Solution:

    def generateMatrix(self, n):

        matrix = [[None for i in range(n)] for i in range(n)]
        seen = [[0 for i in range(n)] for i in range(n)]
        # Traversal using simulation method

        x, y = 0, 0
        dir_r = [0, 1, 0, -1]
        dir_c = [1, 0, -1, 0]

        dir_ind = 0
        count = 1
        for i in range(n*n):
            matrix[x][y] = count
            seen[x][y] = True

            cr = x+dir_r[dir_ind]
            cc = y+dir_c[dir_ind]

            if 0 <= cr and cr < n and 0 <= cc and cc < n and not (seen[cr][cc]):
                x = cr
                y = cc

            else:
                dir_ind = (dir_ind+1) % 4
                x += dir_r[dir_ind]
                y += dir_c[dir_ind]

            count += 1
        return matrix


sln = Solution()

print(sln.generateMatrix(3))
