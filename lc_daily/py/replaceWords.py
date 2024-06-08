class Solution:
    def replaceWords(self, dictionary, sentence):
        dictionary = set(dictionary)
        sentence = sentence.split()
        for i, word in enumerate(sentence):
            for j in range(1, len(word)):
                if word[:j] in dictionary:
                    sentence[i] = word[:j]
                    break
        return " ".join(sentence)


sln = Solution()
print(sln.replaceWords(["cat", "bat", "rat"],
      "the cattle was rattled by the battery"))
