class Sol:
    def reductionOperations(self, nums):
        nums.sort(reverse=True)
        l = 0
        r = 1
        count = 0

        while l < len(nums)-1:
            if nums[l] != nums[r]:
                nums[l] = nums[r]
                count += 1

            if nums[l] == nums[-1]:
                l += 1
                r = l+1
            else:
                r += 1
        return count


sln = Sol()
print(sln.reductionOperations([1, 1, 2, 2, 3]))
