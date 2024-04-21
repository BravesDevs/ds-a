from collections import defaultdict


class Solution:
    def validPath(self, n, edges, source, destination):
        paths = defaultdict(list)
        for u, v in edges:
            paths[u].append(v)
            paths[v].append(u)

        visited = set()

        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for v in paths[node]:
                if v not in visited and dfs(v):
                    return True

        return dfs(source)


sln = Solution()
print(sln.validPath(10, [[0, 7], [0, 8], [6, 1], [2, 0], [
      0, 4], [5, 8], [4, 7], [1, 3], [3, 5], [6, 5]], 7, 5))
