class Solution:
    def diagonalSum(self, mat):
        init = 0
        total = 0
        N = len(mat)
        for init in range(N):
            total += mat[init][init]

        for init in range(N-1, -1, -1):
            if init != (N-1)-init:
                total += mat[init][(N-1)-init]
        return total


sln = Solution()
print(sln.diagonalSum([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]]))
