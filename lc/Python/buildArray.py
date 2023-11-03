class Solution:
    def buildArray(self, target, n):
        result = []
        resultTarget = []
        for i in range(1, n+1):
            if resultTarget == target:
                return result
            elif i in target:
                result.append("Push")
                resultTarget.append(i)

            else:
                result.append("Push")
                result.append("Pop")
        return result


sln = Solution()
print(sln.buildArray([2, 3, 4], 4))
