
class Solution:
    def minimumTimeToInitialState(self, word, k):
        initial_word = word
        n = len(word)
        for seconds in range(1, n + 1):
            prefix_removed = word[:k]
            suffix_added = word[:k]
            word = word[k:] + suffix_added
            if word == initial_word:
                return seconds
        return -1


sln = Solution()
print(sln.minimumTimeToInitialState("abacaba", 4))
