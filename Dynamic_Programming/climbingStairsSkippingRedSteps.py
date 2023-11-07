class Solution:
    def climbingBySkippingRedStairs(self, n, k, rs):
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            if i in rs:
                continue
            for j in range(k+1):
                if i-j < 0:
                    continue
                dp[i] += dp[i-j]
        print(dp)


sln = Solution()
print(sln.climbingBySkippingRedStairs(7, 3, [1, 3, 4]))
