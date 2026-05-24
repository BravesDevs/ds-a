class Solution:
    def findLength(self, nums1, nums2):
        # Use dynamic programming with O(len(nums2)) space.
        # dp[j] stores length of longest common suffix starting at nums1[i] and nums2[j]
        m, n = len(nums1), len(nums2)
        if m == 0 or n == 0:
            return 0
        dp = [0] * (n + 1)
        maxLength = 0
        for i in range(m - 1, -1, -1):
            # iterate j backwards so dp[j+1] from previous iteration of j is still valid
            for j in range(n - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[j] = dp[j + 1] + 1
                    if dp[j] > maxLength:
                        maxLength = dp[j]
                else:
                    dp[j] = 0
        return maxLength

s=Solution()
print(s.findLength([0,0,0,0,1],[1,0,0,0,0]))