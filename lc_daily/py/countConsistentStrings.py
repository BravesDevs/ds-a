class Solution:
    def countConsistentStrings(self, allowed, words):
        mainSet = set(allowed)
        count = 0
        while len(words):
            wordSet = set(words.pop(0))
            if wordSet.issubset(mainSet):
                count += 1

        return count
