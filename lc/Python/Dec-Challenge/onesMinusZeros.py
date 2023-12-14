import numpy as np


class Sol:
    def onesMinusZeros(self, grid):
        grid = np.array(grid)
        zeroColSum = {}
        zeroRowSum = {}
        onesColSum = {}
        onesRowSum = {}
        result = []
        
        # Calculate row and column sums
        for i in range(len(grid)):
            onesRowSum[i] = sum(grid[i])
            zeroRowSum[i] = len(grid[i]) - onesRowSum[i]
        
        for j in range(len(grid[0])):
            onesColSum[j] = sum(grid[:, j])
            zeroColSum[j] = len(grid[:, j]) - onesColSum[j]
        
        # Calculate result
        for i in range(len(grid)):
            res = []
            for j in range(len(grid[i])):
                res.append(onesRowSum[i] + onesColSum[j] - zeroRowSum[i] - zeroColSum[j])
            result.append(res)
        
        return result


sln = Sol()
print(sln.onesMinusZeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]]))

# onesRowSum = sum(grid[i])
# onesColSum = sum(grid[:, j])
# zerosRowSum = len(grid[i])-onesRowSum
# zerosColSum = len(grid[:, j])-onesColSum
# result[i][j] = onesRowSum + \
#     onesColSum - zerosRowSum-zerosColSum
