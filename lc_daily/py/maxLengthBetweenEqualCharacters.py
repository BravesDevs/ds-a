class Solution:
    def maxLengthBetweenEqualCharacters(self, s):

        startIndex = {}
        endIndex = {}

        for i in range(len(s)):
            if s[i] not in startIndex:
                startIndex[s[i]] = i

        for j in range(len(s)-1, -1, -1):
            if s[j] not in endIndex and s[j] in startIndex:
                endIndex[s[j]] = j

        if startIndex == endIndex:
            return -1

        maxElements = 0
        for i in startIndex:
            maxElements = max(maxElements, (endIndex[i]-startIndex[i])-1)
        return maxElements


sln = Solution()

print(sln.maxLengthBetweenEqualCharacters('cbzxy'))