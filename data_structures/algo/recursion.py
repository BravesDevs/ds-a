class Solution:
    def nSum(self, n):
        def recursive(n):
            if n == 0:
                return 0
            else:
                return n+recursive(n-1)
        return recursive(n)

    def uniquePaths(self, n, m):
        paths = 0

        def traverse(n, m):
            if n == 1 or m == 1:
                return 1
            else:
                return traverse(n, m-1)+traverse(n-1, m)
        return traverse(n, m)


sln = Solution()
# print(sln.nSum(5))

print(sln.uniquePaths(3, 3))
