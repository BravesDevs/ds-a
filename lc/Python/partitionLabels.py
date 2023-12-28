class Solution:
    def partitionLabels(self, s):
        firstIndex = {}
        lastIndex = {}

        for index, element in enumerate(s):
            if element not in firstIndex:
                firstIndex[element] = index

        for i in range(len(s)-1, -1, -1):
            if s[i] not in lastIndex:
                lastIndex[s[i]] = i

        l = r = maxSpan = 0
        res = []
        while r < len(s):
            while r < len(s) and r <= maxSpan:
                maxSpan = max(maxSpan, lastIndex[s[r]])
                r += 1
            res.append((r-l))
            l = r
            maxSpan += 1
            maxSpan = r
        return res


sln = Solution()
print(sln.partitionLabels("eccbbbbdec"))
