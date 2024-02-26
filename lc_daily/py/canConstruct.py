import functools

class Solution:
    def canConstruct(self, ransomNote, magazine):
        magazineElementCount={}

        magazineSet = list(set(magazine))

        for i in magazineSet:
            magazineElementCount[i]=magazine.count(i)
        
        ransomSetElementCount = {}
        
        ransomSet = list(set(ransomNote))
        
        for i in ransomSet:
            ransomSetElementCount[i]=ransomNote.count(i)

        for i in ransomSet:
            if i not in magazineSet:
                return False
            elif magazineElementCount[i]<ransomSetElementCount[i]:
                return False
        return True


        
sln = Solution()
print(sln.canConstruct("aa","aab"))