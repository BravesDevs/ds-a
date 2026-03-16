class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        res = 0
        left = 0
        seen = set()
        for right in range(N):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right - left + 1)
        return res
    
    
sln = Solution()
print(sln.lengthOfLongestSubstring("au"))
