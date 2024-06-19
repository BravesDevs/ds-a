class Solution:
    def judgeSquareSum(self, n):
        res = 0
        i = 1
        while i**i < n:
            res += i**i
            if res == n:
                return True
            i += 1
        return False


sln = Solution()
print(sln.judgeSquareSum(3))
