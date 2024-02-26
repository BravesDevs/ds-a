import math


class Sol:
    def minOperations(self, s):
        count = 0

        for i in range(len(s)):
            if (i % 2 == 0 and s[i] == '1') or (i % 2 != 0 and s[i] == '0'):
                count += 1

        return min(count, len(s)-count)


sln = Sol()
print(sln.minOperations("1100010111"))
