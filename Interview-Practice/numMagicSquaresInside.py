from ast import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(i, j):
            # Check if all numbers 1-9 are present
            s = set()
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    s.add(grid[x][y])
            if s != set(range(1, 10)):
                return False
            
            # All rows, columns, and diagonals should sum to 15
            target = 15
            
            # Check rows
            for x in range(i, i + 3):
                if sum(grid[x][j:j+3]) != target:
                    return False
            
            # Check columns
            for y in range(j, j + 3):
                if sum(grid[x][y] for x in range(i, i + 3)) != target:
                    return False
            
            # Check diagonals
            if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != target:
                return False
            if grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != target:
                return False
            
            return True
        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if isMagicSquare(i, j):
                    count += 1
        return count
    
    

solution = Solution()
print(solution.numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))