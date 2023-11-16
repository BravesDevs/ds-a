class Sol:
    def findDuplicates(self, nums):
        nums.sort()
        p1 = 0
        res = set()
        for i in range(1, len(nums)):
            if nums[p1] == nums[i]:
                res.add(nums[p1])
            p1 += 1
        return list(res)


sln = Sol()
print(sln.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
