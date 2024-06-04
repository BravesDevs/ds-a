from collections import defaultdict


class Solution:
    def longestPalindrome(self, s):
        countMap = defaultdict(int)

        if len(s) <= 1:
            return len(s)

        for i in s:
            countMap[i] += 1
        res = []
        odd_count = 0
        for i in countMap:
            if countMap[i] % 2 != 0:
                odd_count += 1
            res.append(countMap[i])
        return sum(res) - odd_count + (1 if odd_count > 0 else 0)


sln = Solution()
print(sln.longestPalindrome("a"))
