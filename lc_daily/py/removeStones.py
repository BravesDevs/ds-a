from collections import defaultdict


class Solution:
    def removestones(self, stones):

        rowColMap = defaultdict(list)
        colRowMap = defaultdict(list)

        for i, j in stones:
            rowColMap[i].append(j)
            colRowMap[j].append(i)
        res = 0
        visited = set()

        def dfs(i, j):
            visited.add((i, j))
            for x in rowColMap[i]:
                if (i, x) not in visited:
                    dfs(i, x)
            for y in colRowMap[j]:
                if (y, j) not in visited:
                    dfs(y, j)

        for i, j in stones:
            if (i, j) not in visited:
                dfs(i, j)
                res += 1
        return len(stones) - res


sln = Solution()
print(sln.removestones([[0, 1], [1, 0], [1, 1]]))
