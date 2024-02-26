import numpy as np


class Sol:
    def groupThePeople(self, groupSizes):
        mapDict = {}
        res = []
        for index, element in enumerate(groupSizes):
            if not mapDict.get(element):
                mapDict[element] = []
            mapDict[element].append(index)

        for i in mapDict.keys():
            res.extend(np.array_split(mapDict[i], len(mapDict[i])//i))

        return res


sln = Sol()
print(sln.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
