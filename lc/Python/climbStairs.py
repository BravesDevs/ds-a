class Solution:
    climbStairsDict = {}
    def climbStairs(self, n):
        if n<=3:
            return n
            
        if n in self.climbStairsDict:
            return self.climbStairsDict[n]
        
        self.climbStairsDict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return self.climbStairsDict[n]

sln = Solution()
print(sln.climbStairs(4))