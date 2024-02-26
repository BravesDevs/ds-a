class Sol:
    def maxArea(self, h):
        l, r = 0, len(h)-1
        maxArea = 0
        while l < r:
            maxArea = max(maxArea, min(h[l], h[r])*(r-l))

            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return maxArea


sln = Sol()
print(sln.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
