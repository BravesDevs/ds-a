class Solution:
    def sortVowels(self, s):
        vowels = 'aeiouAEIOU'
        vowelInS = [x for x in s if x in vowels]
        chars = list(s)
        vowelInS.sort(reverse=True)

        for index, element in enumerate(chars):
            if element in vowels:
                chars[index] = vowelInS.pop()
        return ''.join(chars)


sln = Solution()
print(sln.sortVowels('lEetcOde'))
