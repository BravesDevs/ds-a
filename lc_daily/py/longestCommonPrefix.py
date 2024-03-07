class Solution:
    def longestCommonPrefix(self, strs):
        strs.sort(key=len)
        min_st = strs.pop(0)
        if not len(min_st):
            return ""
        res = min_st
        while len(strs):
            st = strs.pop(0)
            check = ''
            for i in range(len(st)):
                if i < len(min_st):
                    if i == 0 and st[i] != min_st[i]:
                        return ''
                    elif st[i] == min_st[i]:
                        check += st[i]
                    else:
                        break
            if len(check) < len(res):
                res = check

        return res


sln = Solution()
print(sln.longestCommonPrefix(["cir", "car"]
                              ))
