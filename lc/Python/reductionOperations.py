class Sol:
    def reductionOperations(self, nums):
        nums.sort(reverse=True)
        count = 1
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                ans += count
            count += 1
        return ans


sln = Sol()
print(sln.reductionOperations([1, 1, 2, 2, 3]))
