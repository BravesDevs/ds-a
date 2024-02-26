import math


class Sol:
    def minTimeToVisitAllPoints(self, points):
        distance = 0
        for i in range(1, len(points)):
            distance += max(abs(points[i][0]-points[i-1][0]),
                            abs(points[i][1]-points[i-1][1]))
        return distance


sln = Sol()
print(sln.minTimeToVisitAllPoints([[3, 2], [-2, 2]]))
