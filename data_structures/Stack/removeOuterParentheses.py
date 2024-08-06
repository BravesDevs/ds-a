class Solution:
    def removeOuterParentheses(self, s):
        stack = []
        N = len(s)
        shouldUse = [False]*N

        for i, op in enumerate(s):
            if op == '(':
                stack.append(i)
            else:
                pop_i = stack.pop()
                if len(stack) > 0:
                    shouldUse[i] = True
                    shouldUse[pop_i] = True
        res = ""
        for i, u in enumerate(shouldUse):
            if u:
                res += s[i]
        return res


sln = Solution()
print(sln.removeOuterParentheses("(())"))
