import numpy


class Solution:
    def timeRequiredToBuy(self, tickets, k):
        time = 0
        array = numpy.array(tickets)
        while array[k] > 0:
            time += (array > 0).sum()
            array -= 1
        return time


sln = Solution()
print(sln.timeRequiredToBuy([5, 1, 1, 1], 0))
