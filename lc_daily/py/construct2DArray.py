class Solution:
    def construct2DArray(self, original, m, n):
        if len(original) > m+n:
            return []
        result = []

        for i in range(0, m):
            li = []
            for j in range(0, n):
                if original:
                    li.append(original.pop(0))
            result.append(li)
        return result


sln = Solution()
print(sln.construct2DArray([1, 2], 1, 1))
