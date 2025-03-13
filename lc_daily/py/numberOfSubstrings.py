class Solution:
    def numberOfSubstrings(self,s):
        count=0
        N=len(s)
        l,r=0,2
        resStrings = set()
        
        while r<N:
            string = s[l:r+1]
            if 'a' in string and 'b' in string and 'c' in string:
                resStrings.add(string)
            r+=1
            
        while l<N:
            string=s[l:N]
            if 'a' in string and 'b' in string and 'c' in string:
                resStrings.add(string)
            l+=1
        
        return len(resStrings)
            
        
        
sln = Solution()

print(sln.numberOfSubstrings("abcabc"))        