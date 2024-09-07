class Solution:
    def isSubPath(self, head, root):
        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False
            if head.val != root.val:
                return False
            return dfs(head.next, root.left) or dfs(head.next, root.right)
        if not root:
            return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


sln = Solution()
print(sln.isSubPath([4, 2, 8], [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]))
