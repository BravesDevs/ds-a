class Solution:
    def nearlyPerfect(self, s):
        # return boolean
        l, r = 0, len(s)-1
        isRemoved = False

        while l < r:
            if s[l] != s[r]:
                if isRemoved:
                    return False
                isRemoved = True
                if s[l+1] == s[r]:
                    l += 1
                elif s[l] == s[r-1]:
                    r -= 1
                else:
                    return False
            l += 1
            r -= 1

        return True


sln = Solution()
print(sln.nearlyPerfect("abc")) 
