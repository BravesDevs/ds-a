class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False

        p1 = 0
        sMapped = ''
        for i in s:
            if s.count(i) > t.count(i):
                return False
            while p1 < len(t):
                if t[p1] != i:
                    p1 += 1
                else:
                    sMapped += t[p1]
                    break

        return s == sMapped


sln = Solution()
print(sln.isSubsequence("axb", "ahbgdc"))
