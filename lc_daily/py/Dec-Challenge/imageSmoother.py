import math


class Sol:
    def imageSmoother(self, nums):
        ROWS = len(nums)
        COLS = len(nums[0])

        res = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                total = 0
                neighborSum = 0
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if (i < 0 or i >= len(nums)) or (j < 0 or j >= len(nums[i])):
                            continue
                        else:
                            total += 1
                            neighborSum += nums[i][j]
                res[r][c] = math.floor(neighborSum/total)

        return res


sln = Sol()
print(sln.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]))
