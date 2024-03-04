class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s)//2
        mapA = {}

        for i in s[:mid]:
            if i in 'aeiouAEIOU':
                if i not in mapA:
                    mapA[i] = 0
                mapA[i] += 1

        for i in s[mid:]:
            if i in mapA:
                if mapA[i] == 1:
                    del mapA[i]
                else:
                    mapA[i] -= 1

        return not mapA


sln = Solution()
print(sln.halvesAreAlike("AbCdEfGh"))
