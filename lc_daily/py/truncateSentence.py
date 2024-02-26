class Sol:
    def truncateSentence(self, s, k):
        listSentences = s.split(' ')

        return ' '.join(listSentences[:k])


sln = Sol()
print(sln.truncateSentence("Hello how are you Contestant", 5))
