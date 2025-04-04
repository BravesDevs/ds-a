class Solution:
    def mostPoints(self,questions):
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, skip = questions[i]
            dp[i] = max(dp[i + 1], points + (dp[i + skip + 1] if i + skip + 1 < n else 0))

        return dp[0]


sln = Solution()
print(sln.mostPoints([[3,2],[4,3],[4,4],[2,5]]))
