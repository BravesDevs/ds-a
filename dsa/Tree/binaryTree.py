# A Python class that represents
# an individual node in a Binary Tree
import math
from treelib import Node, Tree
tree = Tree()


class Node:
    def __init__(self, key=None):
        self.left = None
        self.right = None
        self.val = key


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.traversePath = []
        # self.difference= int('inf')

    def addNode(self, data):
        new_node = Node(data)
        if self.root:
            current = self.root

            while current:
                if data > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = new_node
                        return
                else:
                    if current.left:
                        current = current.left
                    else:
                        current.left = new_node
                        return
        else:
            self.root = new_node

#     def minimumAbsoluteDifference(self):
#         traversal = self.inOrderTraversal(self.root)
#         diff = max(traversal)+1
#         for i in range(len(traversal)-1):
#             diff = min(diff, abs(traversal[i]-traversal[i+1]))
#         return diff

#     def preOrderTraversal(self, node):
#         if node is None:
#             return
#         self.traversePath.append(node.val)
#         self.preOrderTraversal(node.left)
#         self.preOrderTraversal(node.right)

#         return self.traversePath

#     def inOrderTraversal(self, node):
#         if node is None:
#             return
#         self.inOrderTraversal(node.left)
#         self.traversePath.append(node.val)
#         self.inOrderTraversal(node.right)

#         return self.traversePath

#     def postOrderTraversal(self, node):
#         if node is None:
#             return
#         self.postOrderTraversal(node.left)
#         self.postOrderTraversal(node.right)
#         self.traversePath.append(node.val)

#         return self.traversePath

    def mapTree(self, root):

        dictMap = {}

        def traverse(node):
            if node is None:
                return
            dictMap[node.val] = {'l': [], 'r': []}

            if node.left is not None:
                dictMap[node.val]['l'].append(node.left.val)

            if node.right is not None:
                dictMap[node.val]['r'].append(node.right.val)

            traverse(node.left)
            traverse(node.right)

        traverse(root)

        print(dictMap)

    def levelOrderTraversal(self, node):
        self.traversePath = [[node.val]]
        queue = [node]

        while True:
            res = []
            resNodes = []

            while len(queue) > 0:
                current = queue.pop()
                if current.left is not None:
                    res.append(current.left.val)
                    resNodes.append(current.left)
                if current.right is not None:
                    res.append(current.right.val)
                    resNodes.append(current.right)
            if len(resNodes) > 0:
                for i in resNodes[::-1]:
                    queue.append(i)
                self.traversePath.append(res)
            else:
                break

        return [sum(x)/len(x) for x in self.traversePath]

    def minimumLevelBinaryTree(self, node):

        if node is None:
            return 0

        count = 1
        countLi = []

        def traverseTree(node, count):
            if node.left is None and node.right is None:
                countLi.append(count)
                return

            count += 1
            if node.left is not None:
                traverseTree(node.left, count)
            if node.right is not None:
                traverseTree(node.right, count)

        traverseTree(node, count)

        return min(countLi)

    def maximumLevelBinaryTree(self, node):

        if node is None:
            return 0

        count = 1
        countLi = []

        def traverseTree(node, count):
            if node.left is None and node.right is None:
                countLi.append(count)
                return

            count += 1
            if node.left is not None:
                traverseTree(node.left, count)
            if node.right is not None:
                traverseTree(node.right, count)

        traverseTree(node, count)

        return max(countLi)

    def isSame(self, p, q):
        def traverseTree(p, q):
            if p is None and q is None:
                return True

            if ((p and not q) or (q and not p)) or (p.val != q.val):
                return False

            return traverseTree(p.left, q.left) and traverseTree(p.right, q.right)

        return traverseTree(p, q)

    def pathSum(self, root, target):
        if root is None:
            return False

        def countVal(node, count):
            if node is None:
                return False

            count += node.val

            if count == target and node.left is None and node.right is None:
                return True

            return countVal(node.left, count) or countVal(node.right, count)

        return countVal(root, 0)

    def diameterOfBinaryTree(self, node):

        res = [0]

        def dfs(root):
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2+left+right)
            return 1 + max(left, right)

        dfs(node)
        return res[0]

    def mergeTwoTrees(self, root1, root2):
        if not root1 and not root2:
            return None

        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0

        node = Node(v1+v2)

        node.left = mergeTwoTrees(
            root1.left if root1 else None, root2.left if root2 else None)
        node.right = mergeTwoTrees(
            root1.right if root1 else None, root2.right if root2 else None)

        return node

    def isSubTree(self, s, t):
        if not t:
            return True
        if not s:
            return False

        if self.sameTree(s, t):
            return True
        return self.isSubTree(s.left, t) or self.isSubTree(s.right, t)

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)

        return False

    def invertBinaryTree(self, root):
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

        return root

    def treeTrace(self, node):
        mapTree = {}

        def trace(node):
            if node is None:
                return
            li = []
            if node.left is not None:
                li.append(node.left.val)
            if node.right is not None:
                li.append(node.right.val)

            mapTree[node.val] = li
            trace(node.left)
            trace(node.right)

        trace(node)

        print(mapTree)

    def binaryTreePaths(self, node):

        result = []

        def dfs(node, st):
            if not node.left and not node.right:
                st += str(node.val)
                result.append(st)
                return

            st += str(node.val)+"->"

            if node.left:
                dfs(node.left, st)
            if node.right:
                dfs(node.right, st)

        dfs(node, "")

        return result

    def isSymmetric(self, root):
        def dfs(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            return (left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left))

        return dfs(root.left, root.right)

    def getHeight(self, node):
        if not node:
            return 0

        return max(self.getHeight(node.left), self.getHeight(node.right))+1

    def isBalanced(self, root):

        if not root:
            return True

        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)

        if abs(lh-rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True

        return False


#     def minDepth(self, root):
#         node_levels = {}
#         traversal = []

#         def traverse(node, level):
#             if node is None:
#                 return

#             node_levels[node.val] = level
#             traversal.append(node.val)
#             traverse(node.left, level + 1)

#             traverse(node.right, level + 1)

#         traverse(root, 1)

#         return traversal

N1 = Node(2)
N2 = Node(1)
N3 = Node(3)
N4 = Node(3)
N5 = Node(3)
N6 = Node(4)
N7 = Node(4)

N1.left = N2
N1.right = N3

# N1.left.left = N4
# N1.left.right = N5

# N1.left.left.left = N6
# N1.left.left.right = N7

tree = Tree()

print(tree.isBalanced(N1))


# tree = Tree()
# tree.create_node("1","1")
# tree.create_node("2","2",parent="1")
# tree.create_node("3","3",parent="1")
# tree.create_node("4","4",parent="2")
# tree.create_node("5","5",parent="2")

# tree.show()
# n1 = Node(1)
# n1.left = Node(2)
# n1.right = Node(3)
# n1.left.left = Node(4)
# n1.left.right = Node(5)


# tree = Tree(n1)
# result = tree.minDepth(tree.root)
# print("Result: ", result)
# result = tree.minimumAbsoluteDifference()
# print(result)
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(2)
# n4 = Node(4)
# n5 = Node(5)
# n6 = Node(5)
# n7 = Node(4)

# n1.left = n2
# n1.right = n3
# n1.left.left = n4
# n1.left.right = n5
# n1.right.left = n6
# n1.right.right = n7


# tree = Tree(n1)
# print(tree.isSymmetric(n1))
# print(tree.binaryTreePaths(n1))
# result = tree.invertBinaryTree(tree.root)
# print(tree.treeTrace(result))
# print(tree.diameterOfBinaryTree(tree.root))
# print(tree.isSubTree(n1, n6))


# n1.left = n2

# n1.right = None

# n1.left.left = n3

# n1.left.right = None

# n1.left.left.left = n4

# n1.left.left.right = None

# n1.left.left.left.left = n5

# n1.left.left.left.right = None

# tree = Tree(n1)
# tree.addNode(9)
# tree.addNode(20)
# tree.addNode(15)
# tree.addNode(7)
# print(tree.minimumLevelBinaryTree(tree.root))
# print(tree.isSame(n1, n4))
# print(tree.mapTree(n1))
# print(tree.pathSum(n1, 0))
# print(tree.maximumLevelBinaryTree(n1))
# tree.treeTrace(tree.root)
# pre_order = tree.preOrderTraversal(tree.root)
# in_order = tree.inOrderTraversal(tree.root)
# post_order = tree.postOrderTraversal(tree.root)
# level_order = tree.levelOrderTraversal(tree.root)

# print("Pre-order: ",pre_order)
# print("In-order: ",in_order)
# print("Post-order: ", post_order)
# print("Level-order: ", level_order)
