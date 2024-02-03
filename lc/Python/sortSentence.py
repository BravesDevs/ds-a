import re


class Solution:
    def sortSentence(self, s):
        s = s.split(' ')
        res = ['']*len(s)
        for i in s:
            res[int(i[-1])-1] = i[:-1]
        return ' '.join(res)


sln = Solution()
print(sln.sortSentence("is2 sentence4 This1 a3"))
