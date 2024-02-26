class Sol:
    def makeEqual(self, words):
        lettersMap = {}
        for i in words:
            for j in i:
                if j not in lettersMap:
                    lettersMap[j] = 0
                lettersMap[j] += 1

        for i in lettersMap:
            if lettersMap[i] % len(words) != 0:
                return False

        return True


sln = Sol()
print(sln.makeEqual(["abc", "aabc", "bc"]))
