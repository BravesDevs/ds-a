class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)

        return True if s == t else False
    
# Path: isAnagram.py

sln = Solution()
print(sln.isAnagram("rat", "car"))