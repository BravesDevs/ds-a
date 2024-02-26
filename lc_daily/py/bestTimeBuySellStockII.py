class Solution:
    def maxProfit(self, prices):
        l,r = 0,1
        maxProfit=0
        while r<len(prices):
            if(prices[r]>prices[l]):
                maxProfit+=prices[r]-prices[l]
            l+=1
            r+=1
        return maxProfit

sln = Solution()
result = sln.maxProfit([1,3,2,8,4,9])
print("Result: ",result)