class pascalTriangle:
    def generate(self, n):
        dp = [[None]*i for i in range(1, n+1)]
        dp[0] = [1]
        if n >= 2:
            dp[1] = [1, 1]

        for i in range(2, n):
            dp[i][0], dp[i][-1] = 1, 1

        for j in range(2, n):
            count = 0
            for k in range(1, len(dp[j])-1):
                dp[j][k] = dp[j-1][count] + dp[j-1][count+1]
                count += 1
        return dp


sln = pascalTriangle()
print(sln.generate(3))
