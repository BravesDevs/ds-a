class Sol:
    def createTargetArray(self, nums, index):
        res = []

        for i in range(len(nums)):
            if nums[index[i]] is None:
                res.append(nums[i])
            else:
                res.insert(index[i], nums[i])
        return res


sln = Sol()
print(sln.createTargetArray([0, 1, 0], [0, 1, 0]))
