class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        fastPtr = 1
        slowPtr = 0
        while fastPtr<=len(s):
            strLen = len(s[slowPtr:fastPtr])
            setLen = len(set(s[slowPtr:fastPtr]))
            
            if strLen == setLen:
                length = strLen if strLen > length else length
                fastPtr+=1
            else:
                slowPtr+=1
        
        print(length)

sln = Solution()
sln.lengthOfLongestSubstring("pwwkew")