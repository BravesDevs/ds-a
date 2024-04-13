class Solution:
    def outlierInterview(self, string):
        sentence = sorted(string.lower().replace('.', '').split(' '), key=len)
        return (' '.join(sentence) + '.').capitalize()


sln = Solution()
print(sln.outlierInterview("This is the sentence."))
