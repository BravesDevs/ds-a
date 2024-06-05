from collections import Counter
from functools import reduce


class Solution:
    def commonChars(self, words):
        countRes = [Counter(word) for word in words]
        common_counter = reduce(lambda x, y: x & y, countRes)
        return list(common_counter.elements())


sln = Solution()
print(sln.commonChars(["bella", "label", "roller"]))
