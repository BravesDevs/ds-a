class Solution:
    def reverseStr(self, s, k):
        res = ""
        for i in range(0, len(s), k):
            if i == i*k:
                res += s[i:i+k][::-1]
            else:
                res += s[i:i+k]
        return res


sln = Solution()
print(sln.reverseStr("abcdefg", 2))  # "bacdfeg"
