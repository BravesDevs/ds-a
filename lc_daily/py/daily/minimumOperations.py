class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minimumOperations(self, root):
        treeVal = []
        treeNodes = []
        treeNodes.append(root)
        treeVal.append([root.val])

        children = []
        childrenVal = []

        res = 0

        def countNumberOfSwapsToSortArray(arr):
            sortedArr = sorted(arr)
            indexMap = {}
            for i in range(len(arr)):
                indexMap[arr[i]] = i
            res = 0
            for i in range(len(arr)):
                if arr[i] != sortedArr[i]:
                    res += 1
                    index = indexMap[sortedArr[i]]
                    arr[i], arr[index] = arr[index], arr[i]
                    indexMap[arr[i]] = i
                    indexMap[arr[index]] = index
            return res

        while treeNodes:
            node = treeNodes.pop(0)
            if node.left:
                childrenVal.append(node.left.val)
                children.append(node.left)
            if node.right:
                childrenVal.append(node.right.val)
                children.append(node.right)
            if childrenVal and (len(treeNodes) == 0):
                res += countNumberOfSwapsToSortArray(childrenVal)
                treeVal.append(childrenVal)
                treeNodes.extend(children)
                children = []
                childrenVal = []

        return res


sln = Solution()
root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.left.left = TreeNode(7)
root.left.right = TreeNode(6)
root.right.left = TreeNode(8)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(9)
root.right.right.right = TreeNode(10)
sln.minimumOperations(root)
