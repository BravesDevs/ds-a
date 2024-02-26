class Solution:
    def __init__(self):
        self.stack = []

    def checkValidParenthesis(self, str):
        parenthesisMap = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for i in str:
            if i not in parenthesisMap:
                self.stack.append(i)
            else:
                if len(self.stack) > 0:
                    if (parenthesisMap[i]==self.stack[-1]):
                        self.stack.pop()
                    else:
                        return False
                else:
                    return False
        return True if len(self.stack) == 0 else False
sln = Solution()
isValidParenthesis = sln.checkValidParenthesis('[')
print("Is Valid: ",isValidParenthesis)

