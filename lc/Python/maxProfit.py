class Solution:
    def maxProfit(self, prices):

        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = max(profit, prices[r]-prices[l])
            r += 1
        return profit


sln = Solution()
print(sln.maxProfit([5, 4, 6, 8]))
