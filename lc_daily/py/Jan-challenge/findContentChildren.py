class Sol:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        count = 0

        for size in s:
            if count < len(g):
                if size >= g[count]:
                    count += 1
            else:
                break
        return count


sln = Sol()
print(sln.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))
