class Solution:
    def diagonalSort(self, mat):
        startRow = len(mat)-1
        startCol = 0

        while startRow >= 0 and startCol < len(mat[0]):
            count = 0
            while count:
                print(mat[startRow][startRow+count])

            startRow -= 1


sln = Solution([[1, 3, 1], [2, 2, 1], [1, 1, 1]])
