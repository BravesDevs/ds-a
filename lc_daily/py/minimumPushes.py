from collections import Counter


class Solution:
    def minimumPushes(self, word):
        counts = [0] * 26
        res = 0
        for c in word:
            counts[ord(c) - ord('a')] += 1

        counts.sort(reverse=True)
        distinct = 0
        for c in counts:
            res += c * (1+distinct//8)
            distinct += 1
        return res


sln = Solution()
print(sln.minimumPushes("abzaqsqcyrbzsrvamylmyxdjl"))
