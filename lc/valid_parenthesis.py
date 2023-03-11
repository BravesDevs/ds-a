def isValid(s):
    bracketDict = {
        '}':'{',
        ')':'(',
        ']':'['
    }
    resultStack = []
    for i in s:
        if(i not in bracketDict):
            resultStack.append(i)
        elif(resultStack and resultStack[-1] == bracketDict[i]):
            resultStack.pop()
        else:
            return False
    return not resultStack
        
print(isValid("()[]{}"))