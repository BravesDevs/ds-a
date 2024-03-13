class Solution:
    def pivotInteger(self, n):
        res = 0
        summation = sum(range(1, n+1))
        for i in range(1, n+1):
            res += i
            if res == summation:
                return i
            summation -= i
        return -1


sln = Solution()
print(sln.pivotInteger(4))
