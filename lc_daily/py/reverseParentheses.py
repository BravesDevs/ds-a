class Solution:
    def reverseParentheses(self, s):
        res = []
        listS = list(s)
        while len(listS):
            element = listS.pop(0)
            if element == ')':
                index = len(res)-1
                while res[index] != '(':
                    index -= 1
                res[index+1:len(res)] = res[index+1:len(res)][::-1]
                res[index] = ''
            else:
                res.append(element)
        s = ''
        for i in res:
            if i not in '()':
                s += i
        return s


sln = Solution()
print(sln.reverseParentheses("(ed(et(oc))el)"))
