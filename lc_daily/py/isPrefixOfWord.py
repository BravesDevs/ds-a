class Solution:
    def isPrefixOfWord(self,sentence, searchWord):
        sentence = sentence.split(" ")
        l,r = 0,len(searchWord)-1

        for index, word in enumerate(sentence):
            if r>len(word):
                continue
            elif word[l:r+1] == searchWord:
                return index+1
        return -1
    

sln = Solution()
print(sln.isPrefixOfWord("i love eating burger","burg"))
                