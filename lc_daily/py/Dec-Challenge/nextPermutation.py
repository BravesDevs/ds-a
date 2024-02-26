class Sol:
    def nextPermutation(self, nums):
        if sorted(nums, reverse=True) == nums:
            sortedNums = sorted(nums)
            for index, element in enumerate(sortedNums):
                nums[index] = element

        else:
            i, j = len(nums)-2, len(nums)-1
            while i >= 0:
                if nums[i] < nums[j]:
                    j -= 1
                i -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums


sln = Sol()
print(sln.nextPermutation([1, 3, 2]))
