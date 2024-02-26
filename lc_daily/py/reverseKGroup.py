class Solution:
    def reverseKGroup(self, nums, k):
        if k == 1:
            return nums
        if len(nums) < k:
            return nums
        else:
            for i in range(0, len(nums), k):
                if len(nums[i:i+k]) < k:
                    break
                else:
                    nums[i:i+k] = nums[i:i+k][::-1]
            return nums


sln = Solution()
print(sln.reverseKGroup([1, 2, 3, 4, 5], 2))
