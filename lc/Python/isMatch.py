import re


class Solution:
    def isMatch(self, s, p):
        try:
            return bool(re.fullmatch(p, s))
        except re.error:
            print(f"Invalid pattern: {p}")
            return False


sln = Solution()

print(sln.isMatch("abc", "a**bc"))  # False
