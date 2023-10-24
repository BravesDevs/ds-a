class Solution(object):
    def findContentChildren(self, g, s):
        gptr = 0
        g.sort()
        s.sort()
        count = 0
        for size in s:
            if gptr < len(g) and size >= g[gptr]:
                count += 1
                gptr += 1

        return count


sln = Solution()

print(sln.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))
