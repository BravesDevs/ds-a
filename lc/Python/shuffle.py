class Sol:
    def shuffle(self, nums):
        if len(nums) <= 3:
            return nums
        result = []
        firstPart = len(nums)//2
        secondPart = firstPart
        for i in zip(nums[:firstPart], nums[secondPart:]):
            result.extend([i[0], i[1]])
        return result


sln = Sol()
print(sln.shuffle([1, 1, 2, 2]))
