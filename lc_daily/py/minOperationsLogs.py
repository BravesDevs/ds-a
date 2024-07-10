class Solution:
    def minOperations(self, logs):
        stack = []
        while len(logs):
            log = logs.pop(0)
            if log == './':
                continue
            elif log == '../':
                if len(stack):
                    stack.pop()
            else:
                stack.append(log)
        return len(stack)


sln = Solution()
print(sln.minOperations(["./", "../", "./"]))
