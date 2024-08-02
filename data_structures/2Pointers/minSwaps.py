class Solution:
    def minSwaps(self, nums):
        N = len(nums)
        res = 0
        total_ones = nums.count(1)

        l = 0

        win_ones, max_win_ones = 0
        for r in range(2*N):

            if nums[r % N]:
                win_ones += 1

            if r-l+1 > total_ones:
                win_ones -= nums[l % N]
                l += 1
            max_win_ones = max(max_win_ones, win_ones)
        return total_ones - max_win_ones


sln = Solution()
print(sln.minSwaps([0, 1, 0, 1, 1, 0, 0]))
