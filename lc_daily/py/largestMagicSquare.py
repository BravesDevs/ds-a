class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        # 
        M, N = len(grid), len(grid[0])

        def isValidSquare(i,j, size):
            target = sum(grid[i][j:j+size])
            for k in range(i, i+size):
                if sum(grid[k][j:j+size]) != target:
                    return False
            for k in range(j, j+size):
                if sum(grid[x][k] for x in range(i, i+size)) != target:
                    return False
            if sum(grid[i+x][j+x] for x in range(size)) != target:
                return False
            if sum(grid[i+x][j+size-1-x] for x in range(size)) != target:
                return False
            return True
        
        for size in range(min(M,N), 0, -1):
            for i in range(M-size+1):
                for j in range(N-size+1):
                    if isValidSquare(i,j,size):
                        return size
        return 1
    
    
s = Solution()
print(s.largestMagicSquare([[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]))