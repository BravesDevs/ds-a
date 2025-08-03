class Solution:
    def generate(self,numRows):
        def dp(i):
            if i==0:
                return [1]
            if i == 1:
                return [1, 1]
            prev_row = dp(i-1)
            current_row = [1]
            for j in range(1, len(prev_row)):
                current_row.append(prev_row[j-1] + prev_row[j])
            current_row.append(1)
            return current_row
        
        return [dp(i) for i in range(numRows)][numRows]


sln = Solution()
print(sln.generate(5))