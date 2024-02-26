class Sol:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


sln = Sol()
print(sln.isAnagram("rat", "car"))
