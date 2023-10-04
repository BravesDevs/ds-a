class Solution:
    def isHappy(self, n):
        while n > 10:
            n = self.isHappy(sum([int(i) ** 2 for i in str(n)]))

        if n == 1:
            return True
        else:
            return False


sln = Solution()
print(sln.isHappy(2))
