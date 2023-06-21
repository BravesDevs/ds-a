class Solution:
    def lengthOfLongestSubstring(self, s):
        l,r = 0,1
        length=1 if len(s)>0 else 0
        while r<len(s):
            if s[r] not in s[l:r]:
                length=max(length,(r-l)+1)
            while s[r] in s[l:r]:
                l+=1
            r+=1
        return length




sln = Solution()
result=sln.lengthOfLongestSubstring("pwwkew")
# print(result)