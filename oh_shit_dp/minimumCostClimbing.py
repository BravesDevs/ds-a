class Solution:
    def paidStairCase(self, n, p):
        dp = [0]*(n+1)

        dp[0] = 0
        dp[1] = p[1]

        for i in range(2, n+1):
            dp[i] = min(dp[i-1], dp[i-2]) + p[i]

        return dp[n]


sln = Solution()

print(sln.paidStairCase(3, [0, 3, 2, 4]))
