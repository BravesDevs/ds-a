from collections import Counter


class Solution:
    def customSortString(self, order, s):
        freq = Counter(s)
        res = ''
        visited = set()

        for i in order:
            if i in s and i not in visited:
                res += i * freq[i]
                visited.add(i)

        for i in s:
            if i not in visited:
                res += i * freq[i]
                visited.add(i)
        return res


sln = Solution()
print(sln.customSortString("cba",
      "cbad"))
