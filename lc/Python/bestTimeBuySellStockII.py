class Solution:
    def maxProfit(self, prices):
        l,r = 0,1
        maxProfit=0
        while r<len(prices):
            if(prices[r]>prices[l]):
                maxProfit+=prices[r]-prices[l]
            l=r
            r+=1
        return maxProfit

sln = Solution()
result = sln.maxProfit([7,6,4,3,1])
print("Result: ",result)