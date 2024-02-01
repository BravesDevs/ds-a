class Solution:
    def countAndSay(self, n):
        num = "1"

        i = 1
        while i < n:
            st = ""
            l, r = 0, 0
            while r < len(num):
                while r < len(num) and num[l] == num[r]:
                    r += 1
                st += str(((r-l)))+num[l]
                l = r
            num = st
            i += 1
        return num


sln = Solution()

print(sln.countAndSay(1))
