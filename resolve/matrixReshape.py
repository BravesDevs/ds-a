from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        N = len(mat) 
        M = len(mat[0])

        if  ((r*c) != (N*M)) or (N==r and M==c):
            return mat

        res = [[0 for _ in range(c)] for _ in range(r)]
        arr = mat.pop(0)

        while arr:
            for i in range(r):
                for j in range(c):
                    res[i][j] = arr.pop(0)
                    if not arr and not mat:
                        return res
                    elif not arr:
                        arr = mat.pop(0)
            if len(mat):
                arr = mat.pop(0)
        return res
            

sln = Solution()
print(sln.matrixReshape([[1,2],[3,4]], 2, 4))
