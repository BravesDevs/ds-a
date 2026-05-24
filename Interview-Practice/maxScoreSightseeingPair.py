class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res=0
        N=len(values)
        cur_max = values[0] - 1
        for j in range(1,N):
            res = max(res, cur_max+values[j])
            cur_max = max(cur_max-1, values[j]-1)
        return res
# Time complexity: O(n)
# Space complexity: O(1)
sln = Solution()
print(sln.maxScoreSightseeingPair([1,3,5]))