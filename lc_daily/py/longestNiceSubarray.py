class Solution:
    def longestNiceSubarray(self,nums):
        def isNice(arr):
            for i in arr:
                if i.lower() not in arr and i.upper() not in arr:
                    return False
            return True
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i+1,n+1):
                if isNice(nums[i:j]):
                    res.append(nums[i:j])
        return max(res,key = len) if res else []
sln = Solution()