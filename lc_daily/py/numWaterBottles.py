class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        res = numBottles
        while numBottles >= numExchange:
            res += numBottles//numExchange
            usedBottles = numExchange * (numBottles//numExchange)
            numBottles = (numBottles % numExchange) + (numBottles//numExchange)
        return res


sln = Solution()
print(sln.numWaterBottles(15, 4))
