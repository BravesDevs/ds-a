class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(s, path, res):
            if len(s) > (4 - len(path)) * 3:
                return
            if not s and len(path) == 4:
                res.append('.'.join(path))
                return
            for i in range(min(3, len(s))):
                cur = s[:i + 1]
                if (len(cur) > 1 and cur[0] == '0') or int(cur) > 255:
                    continue
                backtrack(s[i + 1:], path + [cur], res)
        res = []
        backtrack(s, [], res)
        return res
