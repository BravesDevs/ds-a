import math


class Sol:
    def minEatingSpeed(self, piles, h):
        left = 0
        rangeLi = range(1, max(piles)+1)
        right = len(rangeLi)-1
        res = 0
        while left <= right:
            mid = math.ceil((left+right)/2)

            eatingSpeed = rangeLi[mid]
            eatingTime = 0
            for i in piles:
                eatingTime += math.ceil(i/eatingSpeed)

            if eatingTime <= h:
                right = mid-1
                res = rangeLi[mid]
            else:
                left = mid+1
        return res


sln = Sol()
print(sln.minEatingSpeed([30, 11, 23, 4, 20], 6))
