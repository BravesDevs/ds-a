class Solution:
    def countSubarrays(self, nums, minK, maxK):
        left = 0
        res = 0
        queue = []

        while left < len(nums):
            while left < len(nums) and nums[left] != minK:
                left += 1

            right = left

            while right < len(nums) and nums[right] <= maxK:
                queue.append(nums[right])
                if min(queue) == minK and max(queue) == maxK:
                    res += 1
                right += 1
            left += 1
        return res


sln = Solution()
print(sln.countSubarrays([928799, 888361, 928799, 928799, 928799,
      928799, 124173, 93094, 399240, 946505, 93094, 93094, 585816], 93094, 928799))
