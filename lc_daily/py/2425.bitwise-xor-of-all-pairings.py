#
# @lc app=leetcode id=2425 lang=python
#
# [2425] Bitwise XOR of All Pairings
#

# @lc code=start
class Solution(object):
    def xorAllNums(self, nums1, nums2):
        res = 0

        if len(nums2) % 2 == 1:
            for n in nums1:
                res ^= n
        if len(nums1) % 2 == 1:
            for n in nums2:
                res ^= n
        return res

        
# @lc code=end

