class Sol:
    def removePalindromeSub(self, s):
        if not s:
            return 0

        if s == s[::-1]:
            return 1

        return 2


sln = Sol()

print(sln.removePalindromeSub("ababa"))
