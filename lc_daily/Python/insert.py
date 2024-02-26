class Sol:
    def insert(self, intervals, newInterval):
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),
                               max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res


sln = Sol()
print(sln.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
