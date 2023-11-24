class Sol:
    def maxCoins(self, piles):
        if len(piles) == 3:
            return piles[1]

        piles.sort()
        ans = 0
        for i in range(len(piles)//3, len(piles), 2):
            ans += piles[i]
        return ans


sln = Sol()
print(sln.maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]))
