class Sol:
    def findMatrix(self, nums):
        maxCount = 0

        for i in nums:
            maxCount = max(maxCount, nums.count(i))

        res = [[] for i in range(maxCount)]
        for i in nums:
            for j in res:
                if i not in j:
                    j.append(i)
                    break
        return res


sln = Sol()

print(sln.findMatrix([1, 3, 4, 1, 2, 3, 1]))
