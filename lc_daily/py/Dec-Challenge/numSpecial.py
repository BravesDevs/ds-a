import numpy as np


class Sol:
    def numSpecial(self, mat):
        count = 0
        mat = np.array(mat)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    res = sum(mat[i])+sum(mat[:, j])
                    if res == 2:
                        count += 1
        return count


sln = Sol()
print(sln.numSpecial([[0, 0], [0, 0], [1, 0]]))
