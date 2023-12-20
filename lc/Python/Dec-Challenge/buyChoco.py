class Sol:
    def buyChoco(self, prices, money):
        prices.sort()
        costChoc = 0
        totalChoc = 0
        for i in range(2):
            if prices[i] <= money:
                costChoc += prices[i]
                totalChoc += 1
        return money-costChoc if costChoc <= money and totalChoc == 2 else money


sln = Sol()
print(sln.buyChoco([66, 63, 14, 39, 71, 38, 91], 16))
