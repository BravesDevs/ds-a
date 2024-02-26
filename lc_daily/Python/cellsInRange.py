class Solution:
    def cellsInRange(self, s):
        start, end = s.split(":")
        startCol, startRow = list(start)
        endCol, endRow = list(end)

        startCol = ord(startCol) - ord("A") + 1
        endCol = ord(endCol) - ord("A") + 1

        startRow = int(startRow)
        endRow = int(endRow)

        cells = []

        for col in range(startCol, endCol + 1):
            for row in range(startRow, endRow + 1):
                cells.append(chr(col + ord("A") - 1) + str(row))

        return cells


sln = Solution()

print(sln.cellsInRange("K1:L2"))
