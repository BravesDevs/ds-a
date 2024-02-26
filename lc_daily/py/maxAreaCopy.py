class Solution:

    def maxArea(self, height):
        l, r = 0, len(height)-1
        area = 0
        while l < r:
            area = max(area, min(height[l], height[r])*(r-l))

            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return area


sln = Solution()
print(sln.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
