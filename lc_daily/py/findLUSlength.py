class Solution:
    def isSubsequence(self, s, t):
        t = iter(t)
        return all(c in t for c in s)

    def findLUSlength(self, strs):
        strs.sort(key=len, reverse=True)
        for i, s in enumerate(strs):
            if all(not self.isSubsequence(s, t) for j, t in enumerate(strs) if i != j):
                return len(s)
        return -1


sln = Solution()
print(sln.findLUSlength(["aba", "cdc", "eae"]))
