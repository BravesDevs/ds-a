from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        queue = deque()
        l = r = 0
        result = []
        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()

            if (r+1) >= k:
                result.append(nums[queue[0]])
                l += 1
            r += 1

        return result


sln = Solution()
result = sln.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print("Result: ", result)
