class Sol:
    def diStringMatch(self, s):
        li = [i for i in range(len(s)+1)]
        res = []
        l = 0
        r = len(li)-1
        for i in s:
            if i == 'I':
                res.append(li[l])
                l += 1
            else:
                res.append(li[r])
                r -= 1
        res.extend(li[l:r+1])
        return res


sln = Sol()
print(sln.diStringMatch("DDI"))
