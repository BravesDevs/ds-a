class Solution:
    def titleToNumber(self, s):
        return sum((ord(s[i]) - 64) * (26 ** (len(s) - i - 1)) for i in range(len(s)))

# Time complexity: O(n)
