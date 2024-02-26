class Sol:
    def decompressRLElist(self, nums):
        res = []
        for i in range(0, len(nums), 2):
            res.extend(nums[i]*[nums[i+1]])
        return res


sln = Sol()

print(sln.decompressRLElist([1, 2, 3, 4]))
