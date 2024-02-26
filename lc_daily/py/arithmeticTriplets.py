class Sol:
    def arithmeticTriplets(self, nums, diff):

        res = []

        for index, element in enumerate(nums):
            target1 = element + diff
            target2 = element + (diff*2)
            if target1 in nums and target2 in nums:
                res.extend([index, nums.index(target1), nums.index(target2)])
        return len(res)//3


sln = Sol()

print(sln.arithmeticTriplets([4, 5, 6, 7, 8, 9], 2))
