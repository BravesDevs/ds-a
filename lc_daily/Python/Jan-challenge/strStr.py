class Sol:
    def strStr(self, s, n):
        l, r = 0, len(n)-1
        while r < len(s):
            if s[l:r+1] == n:
                return l
            else:
                l += 1
                r += 1
        return -1


sln = Sol()
print(sln.strStr("mississippi", "issip"))
