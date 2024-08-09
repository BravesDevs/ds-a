class Solution:
    def numMagicSquaresInside(self, grid):

        def isMagicSquare(cube):
            # check if all elements are unique
            elements = []
            for row in cube:
                for element in row:
                    if element not in elements and element > 0 and element < 10:
                        elements.append(element)
                    else:
                        return False

            for row in cube:
                if sum(row) != 15:
                    return False
            for col in range(3):
                if cube[0][col] + cube[1][col] + cube[2][col] != 15:
                    return False
            if (cube[0][0] + cube[1][1] + cube[2][2] != 15) and (cube[0][2] + cube[1][1] + cube[2][0] != 15) and (len(elements) != 9):
                return False

            return True

        # Fetching the 3x3 cubes from Matrix
        ROWS = len(grid)
        COLS = len(grid[0])
        cubes = []
        for r in range(ROWS-2):
            for c in range(COLS-2):
                elements = []
                for x in range(3):
                    rElements = []
                    for y in range(3):
                        rElements.append(grid[r+x][c+y])
                    elements.append(rElements)
                cubes.append(elements)

        res = 0
        for cube in cubes:
            if isMagicSquare(cube):
                res += 1
        return res


sln = Solution()
print(sln.numMagicSquaresInside([[5, 5, 5], [5, 5, 5], [5, 5, 5]]
                                ))
