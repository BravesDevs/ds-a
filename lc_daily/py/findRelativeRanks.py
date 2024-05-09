from collections import defaultdict


class Solution:
    def findRelativeRanks(self, score):

        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        score_copy = score.copy()

        top_three_indices = sorted(
            range(len(score_copy)), key=lambda i: score_copy[i], reverse=True)[:3]

        for i, index in enumerate(top_three_indices):
            score_copy[index] = medals[i]

        for i in range(3, len(score_copy)):
            score_copy[i] = str(i + 1)

        return score_copy


sln = Solution()
print(sln.findRelativeRanks([1]))
