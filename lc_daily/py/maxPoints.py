class Solution:
    def maxPoints(self, points):
        if len(points) == 1:
            return 1
        if len(points) == 2:
            return 2
        max_points = 0
        for i in range(len(points)):
            p1 = points[i]
            for j in range(i + 1, len(points)):
                p2 = points[j]
                if p1[0] == p2[0]:
                    slope = float('inf')
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                count = 2
                for k in range(j + 1, len(points)):
                    p3 = points[k]
                    if p1[0] == p3[0]:
                        if p2[0] == p3[0]:
                            count += 1
                    else:
                        if (p3[1] - p1[1]) / (p3[0] - p1[0]) == slope:
                            count += 1
                if count > max_points:
                    max_points = count
        return max_points


sln = Solution()
print(sln.maxPoints([[1, 1], [2, 2], [3, 3]]))
