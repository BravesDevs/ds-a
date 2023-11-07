class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minReach = []
        for di, si in zip(dist, speed):
            minReach.append(math.ceil(di/si))
        minReach.sort()
        count = 0

        for i in range(len(minReach)):
            if i >= minReach[i]:
                return count
            count += 1
        return count
