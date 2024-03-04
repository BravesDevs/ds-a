class Solution:
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        maxScore = 0
        l=0
        r=len(tokens)-1
        score=0
        while l<=r:
            if score>=0 and power>=tokens[l]:
                score+=1
                power-=tokens[l]
                l+=1
            elif power<tokens[l] and score>=1:
                score-=1
                power+=tokens[r]
                r-=1
            else:
                break
            maxScore = max(maxScore,score)
        return maxScore

sln = Solution()
print(sln.bagOfTokensScore([200,100],150))