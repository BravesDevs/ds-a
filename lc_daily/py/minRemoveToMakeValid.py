class Solution:
    def minRemoveToMakeValid(self, s):
        stack = []
        indices = []
        for index, element in enumerate(s):
            if element == '(':
                stack.append(element)
                indices.append(index)
            if element == ')':
                if len(stack) and stack[-1] == '(':
                    stack.pop()
                    indices.pop()
                else:
                    indices.append(index)
                    stack.append(element)

        stli = list(s)

        while len(stack):
            ch = stack.pop()

            for i in range(len(stli)):
                if stli[i] == ch:
                    stli[i] = ''
                    break
        return ''.join(stli)


sln = Solution()
print(sln.minRemoveToMakeValid("())()((("))
