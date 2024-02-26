class Sol:
    def spiralOrder(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        visited = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        cr = 0
        cc = 0

        di = 0

        x = 0
        y = 0

        count = 0
        while count < rows*cols:
            res.append(matrix[x][y])
            visited.append((x, y))
            cr = x + dr[di]
            cc = y + dc[di]
            if 0 <= cr and cr < rows and 0 <= cc < cols and (cr, cc) not in visited:
                x = cr
                y = cc
            else:
                di = (di+1) % 4
                x += dr[di]
                y += dc[di]
            count += 1
        return res


sln = Sol()
print(sln.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
