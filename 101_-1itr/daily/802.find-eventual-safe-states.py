#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#

# @lc code=start
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        location = [0] * len(graph)
        def check_safe(i):
            if location[i]==1:
                return False
            if location[i]==2:
                return True

            location[i] = 1
            for j in graph[i]:
                if not check_safe(j):
                    return False
            location[i] = 2
            return True

        for i in range(len(graph)):
            if check_safe(i):
                res.append(i)
        return res            
        
       
# @lc code=end

