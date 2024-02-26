class Solution(object):
    def wordPattern(self, pattern, s):
        mappingDict = {}
        patternLi = list(pattern)
        wordsLi = s.split(' ')
        if len(patternLi) != len(wordsLi):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in mappingDict and wordsLi[i] not in mappingDict.values():
                mappingDict[pattern[i]] = wordsLi[i]
        
        for i in range(len(pattern)):
            if pattern[i] in mappingDict and mappingDict[pattern[i]] != wordsLi[i]:
                return False

            # Check if the value is in the dictionary and mapped to same key if not return False
            if pattern[i] not in mappingDict and wordsLi[i] in mappingDict.values():
                return False

        return True

sln = Solution()

print(sln.wordPattern("aaa","dog dog dog dog"))