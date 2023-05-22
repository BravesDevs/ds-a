class Solution:
    def maxProfit(self, prices):
        l,r=0,1

        maxProfit=0

        while r<len(prices):
            if prices[l]<prices[r]:
                maxProfit=max(maxProfit,prices[r]-prices[l])
            else:
                l=r
            r+=1
        return maxProfit

sln = Solution()
profit = sln.maxProfit([7,5,6,2,1])


print(profit)