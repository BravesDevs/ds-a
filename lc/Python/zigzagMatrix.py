class Solution:
    def zigzag(self, n):
        x, y = 0, 0

        result = [[-99 for i in range(n)] for i in range(n)]
        seen = [[0 for i in range(n)] for i in range(n)]
        di = 0
        dir_row = [0, 1, 0]
        dir_col = [1, -1, 1]

        for i in range(1, (n*3)):
            if seen[-1][-1] == True:
                return result
            result[x][y] = i
            seen[x][y] = True

            cal_row = x + dir_row[di]
            cal_col = y + dir_col[di]

            if 0 <= cal_row and cal_row < n and 0 <= cal_col and cal_col < n and not (seen[cal_row][cal_col]):
                x = cal_row
                y = cal_col
            else:
                di = (di+1) % 3
                x += dir_row[di]
                y += dir_col[di]

        return result


sln = Solution()
print(sln.zigzag(4))
