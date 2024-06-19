class Solution:
    def getRow(self, rowIndex: int):
        def getRow(rowIndex):
            if rowIndex == 0:
                return [1]
            if rowIndex == 1:
                return [1, 1]
            prev = getRow(rowIndex-1)
            return [1] + [prev[i] + prev[i+1] for i in range(len(prev)-1)] + [1]
        return getRow(rowIndex)