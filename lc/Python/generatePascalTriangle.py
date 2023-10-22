class Solution:
    def generate(self, numRows):
        result = [[1]]
        for i in range(numRows):
            for j in range(numRows-i+1):
                for j in range(i+1)

sln = Solution()
print(sln.generate(6))
