class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromic_substrings = []
        
        for i in range(len(s)): 
            ptr_expand_left, ptr_expand_right = i,i
            
            while ptr_expand_left>=0 and ptr_expand_right<len(s) and s[ptr_expand_left] == s[ptr_expand_right]:
                palindromic_substrings.append(s[ptr_expand_left:ptr_expand_right+1])
                ptr_expand_left -= 1
                ptr_expand_right += 1

            ptr_expand_left, ptr_expand_right = i, i+1
            while ptr_expand_left>=0 and ptr_expand_right<len(s) and s[ptr_expand_left] == s[ptr_expand_right]:
                palindromic_substrings.append(s[ptr_expand_left:ptr_expand_right+1])
                ptr_expand_left -= 1
                ptr_expand_right += 1
        print("Longest palindromic Substring is: ", max(palindromic_substrings, key=len))
            
sln = Solution()
sln.longestPalindrome("babaddtattarrattatddetartrateedredividerb")