class Solution:
    def maxProfit(self, prices,fee):
        l,r=0,1
        maxProfit=0
        while r<len(prices):
            if prices[r]<prices[l]:
                l+=1
                r+=1
            else:
                totalSum=(prices[r]-prices[l])-fee
                if totalSum<=0:
                    r+=1
                else:
                    l=r
                    r+=1
                    maxProfit+=totalSum
                
        return maxProfit

sln = Solution()
profit = sln.maxProfit([1,3,2,8,4,9],2)


print(profit)