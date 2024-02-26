class Sol:
    def moveZeroes(self, nums):
        i = j = 0

        while j < len(nums):
            if nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums


sln = Sol()
print(sln.moveZeroes([0, 1, 0, 3, 12]))
