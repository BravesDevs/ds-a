class Sol(object):
    def countCharacters(self, words, chars):
        summation = 0
        for word in words:
            mapSet = set()
            for letter in word:
                if letter in mapSet:
                    continue
                if (word.count(letter) > chars.count(letter)):
                    break
                mapSet.add(letter)
            else:
                summation += len(word)
        return summation


sln = Sol()
print(sln.countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"))
