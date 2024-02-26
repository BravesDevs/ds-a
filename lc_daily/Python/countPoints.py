import math


class Sol:
    def countPoints(self, points, queries):
        res = []
        for i in queries:
            count = 0
            for j in points:
                distance = math.sqrt(pow(j[0]-i[0], 2)+pow(j[1]-i[1], 2))
                count = count+1 if distance <= i[-1] else count
            res.append(count)
        return res


sln = Sol()
print(sln.countPoints([[1, 3], [3, 3], [5, 3], [2, 2]],
      [[2, 3, 1], [4, 3, 1], [1, 1, 2]]))
