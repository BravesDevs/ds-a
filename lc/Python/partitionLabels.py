class Solution:
    def partitionLabels(self, s):
        firstIndex = {}
        lastIndex = {}

        for index, element in enumerate(s):
            if element not in firstIndex:
                firstIndex[element] = index
            lastIndex[element] = index
            

        l = r = 0
        res = [0]
        while r < len(s):
            pos = l
            while l <= r:
                r = max(r, lastIndex[s[l]])
                l += 1

            res.append((r-pos)+1)
            r = pos = l

        return res[1:]


sln = Solution()
print(sln.partitionLabels("eccbbbbdec"))
