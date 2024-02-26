import copy


class Sol:
    def rotate(self, matrix):
        newMat = copy.deepcopy(matrix)
        length = len(matrix)
        for i in range(length):
            for j in range(length):
                matrix[i][j] = newMat[(length-1)-j][i]

        return matrix


sln = Sol()
print(sln.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
