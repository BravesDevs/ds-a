class Solution:
    def magicalString(self, n):
        s = " 122"

        for i in range(3, n + 1):
            if i & 1:
                s += int(s[i]) * '1'
            else:
                s += int(s[i]) * '2'

        return s[:n + 1].count('1')


sln = Solution()
print(sln.magicalString(6))
