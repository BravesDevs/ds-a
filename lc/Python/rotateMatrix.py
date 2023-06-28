import copy
class Solution(object):
    def rotate(self, matrix):
        reversedMatrix = copy.deepcopy(matrix[::-1])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j]=reversedMatrix[j][i]
        return matrix

sln = Solution()
result = sln.rotate([[1,2,3],[4,5,6],[7,8,9]])
print("Result: ",result)