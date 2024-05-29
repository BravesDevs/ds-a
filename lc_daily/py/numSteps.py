class Solution:
    def numSteps(self, s):
        steps = 0
        n = int(s, 2)
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n += 1
            steps += 1

        return steps


sln = Solution()
print(sln.numSteps("1101"))
