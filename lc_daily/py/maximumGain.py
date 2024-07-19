class Solution:
    def maximumGain(self, s, x, y):
        res = []
        score1 = 0
        score2 = 0
        for c in s:
            top = res[-1] if len(res) else ''
            if top+c == 'ba':
                score1 += y
                res.pop()
            else:
                res.append(c)
        res1 = []
        for c in res:
            top = res1[-1] if len(res1) else ''
            if top+c == 'ab':
                score1 += x
                res1.pop()
            else:
                res1.append(c)

        return score1


sln = Solution()
result = sln.maximumGain("cdbcbbaaabab", 4, 5)
print(result)
