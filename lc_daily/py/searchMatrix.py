class Sol:
    def searchMatrix(self, matrix, target):
        l = 0
        r = len(matrix)-1

        while l <= r:
            mid = (l+r)//2

            if target in matrix[mid]:
                return True
            elif target <= matrix[mid][0]:
                r = mid-1
            else:
                l = mid+1
        return False


sln = Sol()
print(sln.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
