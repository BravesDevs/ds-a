class Sol:
    def arrayStringsAreEqual(self, word1, word2):
        st1 = ''.join(word1)
        st2 = ''.join(word2)
        return st1 == st2


sln = Sol()
print(sln.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
