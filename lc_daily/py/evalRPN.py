class Solution:
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i not in '+-*/':
                stack.append(i)
            else:
                right = stack.pop()
                left = stack.pop()
                expr = left + i + right
                stack.append(str(int(eval(expr))))

        return stack.pop()


sln = Solution()
print(sln.evalRPN(["4", "13", "5", "/", "+"]))
