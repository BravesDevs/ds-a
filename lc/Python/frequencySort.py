from collections import Counter


class Solution:
    def frequencySort(self, s):
        freq = Counter(s)
        sortedFreq = sorted(
            freq.items(), key=lambda item: item[1], reverse=True)
        st = ""
        for i in sortedFreq:
            st += i[0]*i[1]
        return st


sln = Solution()
print(sln.frequencySort("Aabb"))
