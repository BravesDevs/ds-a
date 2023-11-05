class Solution:
    def climbMaxKStairs(self, n, k):
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, k+1):
                if i-j < 0:
                    continue
                dp[i] += dp[i-j]
        print(dp)


sln = Solution()

print(sln.climbMaxKStairs(2, 4))
