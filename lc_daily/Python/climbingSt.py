class Solution:
    def __init__(self):
        self.climbMap = {}

    def climbStairs(self,n):
        if n<=3:
            return n

        if self.climbMap.get(n) is not None:
            return self.climbMap[n]
        else:
            self.climbMap[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.climbMap.get(n)
        
sln = Solution()
print(sln.climbStairs(44))