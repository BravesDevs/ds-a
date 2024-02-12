from collections import Counter


class Solution:
    def majorityElement(self, nums):
        freq = Counter(nums)
        res = 0
        count = 0
        for i in freq:
            if freq[i] > count:
                res = i
                count = freq[i]
        return res


sln = Solution()
print(sln.majorityElement([2, 2, 1, 1, 1, 2, 2]))
