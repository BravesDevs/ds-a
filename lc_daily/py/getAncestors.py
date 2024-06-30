from collections import defaultdict


class Solution:
    def getAncestors(self, n, edges):
        graph = defaultdict(list)
        res = {i: [] for i in range(n)}

        for edge in edges:
            graph[edge[0]].append(edge[1])

        def dfs(parent, child):
            res[child].extend(res[parent])
            if parent not in res[child]:
                res[child].append(parent)
            res[child] = sorted(set(res[child]))
            if child in graph:
                parent = child
                for child in graph[parent]:
                    dfs(parent, child)
            else:
                return
            

        for edge in edges:
            dfs(edge[0], edge[1])

        res = dict(sorted(res.items()))
        return list(res.values())


sln = Solution()
print(sln.getAncestors(
    9, [[7, 5], [2, 5], [0, 7], [0, 1], [6, 1], [2, 4], [3, 5]]))
