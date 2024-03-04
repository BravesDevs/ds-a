class Sol:
    def transpose(self, matrix):
        res = [[0]*len(matrix) for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res[j][i] = matrix[i][j]
        return res


sln = Sol()
print(sln.transpose([[1, 2, 3], [4, 5, 6]]))
