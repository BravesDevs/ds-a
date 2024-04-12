class Solution:
    def outlierInterview(self, string):
        sentence = string.lower().replace('.', '').split(' ')
        sentence.sort(key=len)
        res = (' '.join(sentence) + '.').capitalize()
        return res


sln = Solution()
print(sln.outlierInterview("This is the sentence."))
