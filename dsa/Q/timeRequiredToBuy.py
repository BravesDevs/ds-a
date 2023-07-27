from functools import reduce


class Solution(object):

    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        secs = 0 
        i = 0
        while tickets[k] != 0:
            if tickets[i] != 0:
                tickets[i] -= 1
                secs += 1
            i = (i + 1) % len(tickets)
            
        return secs


sln = Solution()
result = sln.timeRequiredToBuy([84, 49, 5, 24, 70, 77, 87, 8], 3)
print(result)


# lis = [2, 3, 2]
# arr1 = reduce(lambda a: a-1, lis)
# print(arr1)
