from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        res = 0
        for query in queries:
            if sum(nums)==0:
                break
            res+=1
            for i in range(query[0], query[1]+1):
                nums[i] -= min(nums[i], query[2])
        return res if sum(nums)==0 else -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.minZeroArray([4,3,2,1], [[1,3,2],[0,2,1]]))

