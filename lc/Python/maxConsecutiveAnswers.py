class Solution:
    def maxConsecutiveAnswers(self, answerKey, k):
        countF = 0
        countT = 0
        i = 0
        j = 0
        ans = 0
        
        while j < len(answerKey):
            if answerKey[j] == 'F':
                countF += 1
            else:
                countT += 1
            
            while min(countF, countT) > k:
                if answerKey[i] == 'F':
                    countF -= 1
                else:
                    countT -= 1
                
                i += 1
            
            ans = max(ans, countF + countT)
            j += 1
        
        return ans

        

sln=Solution()
result = sln.maxConsecutiveAnswers('TTFF',2)
print(result)