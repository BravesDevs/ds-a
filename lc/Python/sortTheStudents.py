import numpy as np


class Sol:
    def sortTheStudents(self, score, k):
        array = np.array(score)
        originalCol = array[:, k]
        sortedCol = sorted(originalCol, reverse=True)
        print(sortedCol)
        res = [[None] * len(score[0]) for i in range(len(score))]

        for index, element in enumerate(originalCol):
            res[sortedCol.index(originalCol[index])] = score[index]

        return res

    def sortTheStudents1(self, score, k):
        return sorted(score, key=lambda s: s[k], reverse=True)


sln = Sol()
print(sln.sortTheStudents1([[3, 4], [5, 6]], 0))
