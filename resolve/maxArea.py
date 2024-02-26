class Solution:
    def maxArea(self, height):

        p1 = 0

        p2 = len(height)-1

        maxHeight = 0
        while p1 < p2:
            maxHeight = max(maxHeight, min(height[p1], height[p2])*(p2-p1))

            if height[p1] <= height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return maxHeight


sln = Solution()

print(sln.maxArea([2, 3, 4, 5, 18, 17, 6]))
