class Solution:
    def minSteps(self, n):
        cache = {}

        def backtrack(count, paste):
            if count == n:
                return 0
            if count > n:
                return 1000

            if (count, paste) in cache:
                return cache[(count, paste)]
            # Paste
            res1 = 1+backtrack(count+paste, paste)
            # Copy and Paste
            res2 = 2+backtrack(count+count, count)
            cache[(count, paste)] = min(res1, res2)

            return cache[(count, paste)]
        if n == 1:
            return 0

        return 1 + backtrack(1, 1)


sln = Solution()
print(sln.minSteps(3))
