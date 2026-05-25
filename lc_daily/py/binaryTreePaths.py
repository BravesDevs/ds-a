# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res: List[str] = []

        def dfs(node: Optional[TreeNode], path: str) -> None:
            if not node:
                return
            current = path + str(node.val)
            if not node.left and not node.right:
                res.append(current)
                return
            if node.left:
                dfs(node.left, current + "->")
            if node.right:
                dfs(node.right, current + "->")

        dfs(root, "")
        return res
            

sln=Solution()
# ["1->2","1->3->4"]

print(sln.binaryTreePaths(TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4)))))
