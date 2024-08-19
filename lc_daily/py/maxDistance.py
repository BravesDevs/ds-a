import math


class Solution:
    def maxDistance(self, arrays):
        minElement = math.inf
        maxElement = -math.inf

        for i in range(1, len(arrays)):
            arr = arrays[i]
            if i[0] < minElement:
                minElement = arr[0]
                continue
            if i[-1] > maxElement:
                maxElement = i[-1]
                continue
        return maxElement-minElement


sln = Solution()
print(sln.maxDistance([[1, 4], [0, 5]]))
