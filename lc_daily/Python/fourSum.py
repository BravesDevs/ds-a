class Solution(object):
    def fourSum(self, nums, target):
        res = set()
        nums.sort()
        for k in range(0, len(nums)-2):
            for i in range(k+1, len(nums)):

                l, r = i+1, len(nums)-1

                while l < r:
                    summ = nums[k] + nums[i] + nums[l] + nums[r]

                    if summ == target:
                        res.add(tuple([nums[k], nums[i], nums[l], nums[r]]))
                        l += 1
                    elif summ < target:
                        l += 1
                    else:
                        r -= 1
        return list(res)


sln = Solution().fourSum([2, 2, 2, 2, 2], 8)
print(sln)
