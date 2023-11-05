class Solution:
    def getWinner(self, arr, k) -> int:

        if len(arr) < k:
            return max(arr)
        winCount = {}

        while True:
            winner = max(arr[0], arr[1])
            loser = min(arr[0], arr[1])
            count = winCount.get(winner, 0) + 1

            if count >= k:
                return winner
            winCount[winner] = count
            arr[0] = winner
            arr.append(loser)
            del arr[1]


sln = Solution()
print(sln.getWinner([1, 11, 22, 33, 44, 55, 66, 77, 88, 99], 10))
