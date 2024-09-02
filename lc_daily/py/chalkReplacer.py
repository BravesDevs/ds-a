class Solution:
    def chalkReplacer(self, chalk, k):
        total = sum(chalk)

        if not k%total:
            return 0

        left = k%total

        for index in range(len(chalk)):
            left-=chalk[index]

            if left < 0:
                return index


sln = Solution()
print(sln.chalkReplacer([3, 4, 1, 2], 25))
