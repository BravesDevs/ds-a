class Solution:
    def climbStairs(self, n):
        dp = [1, 1, None]

        if n <= 2:
            return dp[n]
        for i in range(2, n+1):
            dp[i % 3] = dp[(i-1) % 3] + dp[(i-2) % 3]
        return dp[n % 3]


sln = Solution()

print(sln.climbStairs(3))
