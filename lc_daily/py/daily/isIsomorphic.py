class Solution:
    def isIsomorphic(self, s, t):
        mapping = {}
        visited = set()

        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                if t[i] in visited:
                    return False
            visited.add(t[i])
            mapping[s[i]] = t[i]
        return True


sln = Solution()
print(sln.isIsomorphic("badc", "baba"))
