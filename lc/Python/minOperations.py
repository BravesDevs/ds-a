import numpy as np


class Sol:
    def minOperations(self, boxes):
        boxes = np.array(list(boxes))
        indices = np.where(boxes == '1')[0]
        res = []
        for index, element in enumerate(boxes):
            summation = 0
            for i in indices:
                if index != i:
                    summation += abs(index-i)
            res.append(summation)
        return res


sln = Sol()
print(sln.minOperations("001011"))
