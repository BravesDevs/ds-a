from collections import defaultdict
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res=[]
        countSet = defaultdict(int)
        N = len(A)
        for i in range(N):
            countSet[A[i]]+=1
            countSet[B[i]]+=1
            count=0
            for key in countSet:
                if countSet[key]==2:
                    count+=1
                    
            res.append(count)
            
        return res



sln = Solution()
print(sln.findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))