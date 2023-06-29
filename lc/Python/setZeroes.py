import numpy as np
class Solution(object):
    def setZeroes(self, matrix):
        array = np.array(matrix)
        indices = np.argwhere(array == 0)
        print(indices)
        if len(indices)==0:
            return matrix
        else:
            # For Rows
            rowsDone=-1
            for element in indices:
                if element[0]!=rowsDone:
                    rowsDone=element[0]
                    matrix[element[0]]=[0]*len(matrix[0])
            # For Cols
            colsDone=-1
            for element in indices:
                if element[1] != colsDone:
                    for i in range(len(matrix)):
                        matrix[i][element[1]]=0
        return matrix

sln = Solution()
result = sln.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
print(result)