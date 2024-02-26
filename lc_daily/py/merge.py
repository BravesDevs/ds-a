import operator


class Solution(object):
    def merge(self, intervals):

        intervals = sorted(
            intervals, key=operator.itemgetter(0), reverse=False)

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i] == [0, 0]:
                continue
            elif intervals[i][0] >= res[-1][0] and intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
                res[-1][0] = min(intervals[i][0], res[-1][0])
            else:
                res.append(intervals[i])
        return res