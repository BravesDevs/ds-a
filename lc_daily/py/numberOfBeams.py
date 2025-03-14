from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        intArr = [row.count('1') for row in bank if row.count('1')>0]
        print(intArr)
        res=0
        for i in range(1,len(intArr)):
            res+=intArr[i]*intArr[i-1]
        return res


sol = Solution()
print(sol.numberOfBeams(["011001","000000","010100","001000"])) # 2