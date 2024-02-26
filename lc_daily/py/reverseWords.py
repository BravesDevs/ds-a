class Sol:
    def reverseWords(self, str):
        strNew = ""
        for i in str.split(' '):
            r = len(i)-1
            stLi = list(i)
            print(stLi)
            r = len(stLi)-1

            while r > len(stLi)//2:
                stLi[(len(stLi)-1)-r], stLi[r] = stLi[r], stLi[(len(stLi)-1)-r]
                r -= 1
            strNew += ''.join(stLi)+' '
        return strNew


sln = Sol()
print(sln.reverseWords("Let's take LeetCode contest"))
