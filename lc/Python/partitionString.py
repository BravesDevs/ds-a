class Sol:
    def partitionString(self, s):
        curSet = set()
        res = 1
        for i in s:
            if i in curSet:
                res += 1
                curSet = set()
            curSet.add(i)
        return res


sln = Sol()
print(sln.partitionString("hdklqkcssgxlvehva"))
