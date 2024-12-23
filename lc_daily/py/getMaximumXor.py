class Solution:
    def getMaximumXor(self, nums, maximumBit):
        n = len(nums)
        res = []
        xor = 0
        for num in nums:
            xor ^= num
            res.append((1 << maximumBit) - 1 ^ xor)
        return res[::-1]
