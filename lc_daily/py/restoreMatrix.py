class Solution:
    def restoreMatrix(self, rowSum, colSum):
        ROWS = len(rowSum)
        COLS = len(colSum)
        res = [[0]*COLS for _ in range(ROWS)]

        for r in range(ROWS):
            res[r][0] = rowSum[r]

        for c in range(COLS):
            cur_col_sum = 0
            for r in range(ROWS):
                cur_col_sum += res[r][c]

            r = 0
            while cur_col_sum > colSum[c]:
                diff = cur_col_sum-colSum[c]
                max_shift = min(diff, res[r][c])
                res[r][c] -= max_shift
                res[r][c+1] += max_shift
                cur_col_sum -= max_shift
                r += 1
        return res


sln = Solution()
print(sln.restoreMatrix([3, 8], [4, 7]))
