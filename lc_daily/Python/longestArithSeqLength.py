class Solution(object):
    def longestArithSeqLength(self, nums):
        lengthOfArray = len(nums)
        dp = [{} for _ in range(lengthOfArray)]

        ans = 0

        for i in range(lengthOfArray):
            dp[i][0]=1
            for j  in range(i):
                diff = nums[i]-nums[j]
                
                if diff not in dp[j]:
                    dp[i][diff]=2
                else:
                    dp[i][diff]=dp[j][diff]+1
            ans = max(ans,max(dp[i].values()))
        return ans


sln = Solution()
result=sln.longestArithSeqLength([3,6,9,12])
print(result)