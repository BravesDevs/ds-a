class Solution:
    def maximumCount(self, nums):
        pos = 0
        neg = 0

        for i in nums:
            if i < 0:
                neg += 1
            else:
                pos += 1
        return max(pos, neg)


sln = Solution()

print(sln.maximumCount([-2, -1, -1, 1, 2, 3]))
