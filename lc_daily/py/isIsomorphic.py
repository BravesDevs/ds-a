class Solution(object):
    def isIsomorphic(self, s, t):
        mappingDict = {}

        for i in range(len(s)):
            if s[i] not in mappingDict:
                if t[i] in mappingDict.values() and [list(mappingDict.values()).index(t[i])]!=s[i]:
                    return False
                mappingDict[s[i]] = t[i]
            elif s[i] in mappingDict and mappingDict[s[i]]!=t[i]:
                return False

        return True
    


sln = Solution()
print(sln.isIsomorphic("paper","title"))
