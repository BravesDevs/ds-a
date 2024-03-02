class Solution:
    def maximumOddBinaryNumber(self, s):

        sorted_s = sorted(s, reverse=True)
        for i in range(len(s) - 1, -1, -1):
            if sorted_s[i] == '1':
                sorted_s[i], sorted_s[-1] = sorted_s[-1], sorted_s[i]
                break
        return ''.join(sorted_s)


sol = Solution()
print(sol.maximumOddBinaryNumber("010"))
