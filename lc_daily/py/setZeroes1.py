class Sol:
    def setZeroes(self, matrix):
        indices = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    indices.append([i, j])
        rowMarked = set()
        colMarked = set()

        for i in indices:
            if i[0] not in rowMarked:
                col = 0
                rowMarked.add(i[0])
                while col < len(matrix[0]):
                    matrix[i[0]][col] = 0
                    col += 1
            if i[1] not in colMarked:
                row = 0
                colMarked.add(i[1])
                while row < len(matrix):
                    matrix[row][i[1]] = 0
                    row += 1
        return matrix


sln = Sol()
print(sln.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
