import heapq


class Solution:
    def smallestChair(self, times, targetFriend):
        times = [(time[0], time[1], i) for i, time in enumerate(times)]
        times.sort()

        used_chair = []

        available_chairs = [i for i in range(len(times))]

        for a, l, i in times:
            while used_chair and used_chair[0][0] <= a:
                _, c = heapq.heappop(used_chair)
                heapq.heappush(available_chairs, c)

            chair = heapq.heappop(available_chairs)
            heapq.heappush(used_chair, (l, chair))

            if i == targetFriend:
                return chair

        return -1


sln = Solution()
print(sln.smallestChair([[1, 4], [2, 3], [4, 6]], 1))
