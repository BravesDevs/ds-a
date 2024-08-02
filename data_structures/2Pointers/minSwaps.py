class Solution:
    def minSwaps(self, nums):
        N = len(nums)
        res = 0
        total_ones = nums.count(1)
        l = 0

        # * Current window ones and maximum window ones
        win_ones, max_win_ones = 0

        # * Making the array circular
        for r in range(2*N):
            # * Maximizing the window size, if the the element is one then increasing the windows size by 1
            if nums[r % N]:
                win_ones += 1
            # * If the window size increased by total_ones window then increment the left pointer
            if r-l+1 > total_ones:
                # ! Decrement the value from the left pointer
                win_ones -= nums[l % N]
                l += 1
            # ? Keep the track of the maximum window ones
            max_win_ones = max(max_win_ones, win_ones)
        return total_ones - max_win_ones


sln = Solution()
print(sln.minSwaps([0, 1, 0, 1, 1, 0, 0]))
