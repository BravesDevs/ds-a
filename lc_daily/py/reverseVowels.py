class Sol:
    def reverseVowels(self, s):
        vowels = [i for i in s if i in 'aeiou' or i in 'AEIOU']

        sLi = list(s)
        for i in range(len(sLi)):
            if sLi[i] in 'aeiou' or sLi[i] in 'AEIOU':
                sLi[i] = vowels.pop()

        return ''.join(sLi)


sln = Sol()
print(sln.reverseVowels("aA"))
