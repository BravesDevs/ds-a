class Sol:
    def reverseString(self, s):
        l, r = 0, len(s)-1
        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
        return s


sln = Sol()
print(sln.reverseString(["H", "a", "n", "n", "a", "h"]))
