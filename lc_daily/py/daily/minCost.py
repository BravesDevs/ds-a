class Sol:
    def minCost(self, colors, neededTime):
        l = res = 0

        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l]
                    l = r
                else:
                    res += neededTime[r]
                    r += 1
            else:
                l = r
        return res


sln = Sol()

print(sln.minCost("aaabbbabbbb", [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]))
