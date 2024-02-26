class Sol:
    def minPairSum(self, nums):
        nums.sort()

        l, r = 0, len(nums)-1
        sum = []
        while l < r:
            sum.append(nums[l]+nums[r])
            l += 1
            r -= 1
        return max(sum)


sln = Sol()
print(sln.minPairSum([3, 2, 4, 1, 1, 5, 1, 3, 5, 1]))
