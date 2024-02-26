import math


class Solution:
    def findTheWinner(self, n, k):
        index = 0
        li = [i+1 for i in range(n)]
        for i in range(n-1):
            index = (index+(k-1)) % n
            li.pop(index)
            if len(li) == 1:
                return li[0]
            n -=1

        return 1

        


sln = Solution()
print(sln.findTheWinner(1, 1))
