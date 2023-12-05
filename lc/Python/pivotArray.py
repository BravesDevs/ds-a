class Sol(object):
    def pivotArray(self, nums, pivot):
        lte = []
        gt = []
        for i in nums:
            if i < pivot:
                lte.append(i)
            elif i > pivot:
                gt.append(i)
        lte.extend([pivot]*nums.count(pivot))
        return lte + gt


sln = Sol()
print(sln.pivotArray([-3, 4, 3, 2], 2))
