class Sol:
    def maxScore(self, s):
        countZeroes = countOnes = 0

        for i in s:
            if i == '1':
                countOnes += 1
        maxCount = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                countZeroes += 1
            else:
                countOnes -= 1
            maxCount = max(maxCount, countOnes+countZeroes)

        return maxCount


sln = Sol()
print(sln.maxScore("00"))
