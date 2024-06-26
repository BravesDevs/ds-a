# A Python class that represents
# an individual node in a Binary Tree
import math
import copy
from collections import defaultdict
# from treelib import Node, Tree
# tree = Tree()
from collections import deque


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
        traversal = [[node.val]]
        queue = [node]

        def levelOrder(node):
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
                    traversal.append(res)
                else:
                    break

        levelOrder(node.left)
        levelOrder(node.right)
        return traversal

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

    def constructMaximumBinaryTree(self, nums):
        if not len(nums):
            return None
        node = Node(max(nums))
        maxPoint = nums.index(max(nums))

        node.left = self.constructMaximumBinaryTree(nums[:maxPoint])
        node.right = self.constructMaximumBinaryTree(nums[maxPoint+1:])

        return node

    def checkTree(self, root):
        total = root.val

        if not root:
            return True
        res = []

        def traversal(node):
            if not node.left and not node.right:
                res.append(node.val)
                return
            else:
                traversal(node.left)
                traversal(node.right)
        traversal(root)

        return sum(res) == total

    def searchBST(self, root, val):
        if not root:
            return []
        res = []

        def traversal(node):
            if not node:
                return
            elif node.val != val:
                traversal(node.left)
                traversal(node.right)
            else:
                res.extend([node, node.left if node.left else None,
                           node.right if node.right else None])
        traversal(root)
        return res

    def countNodes(self, root):
        if not root:
            return 0
        count = [0]

        def dfs(node):
            if not node:
                return
            count[0] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return count[0]

    def isValidBST(self, root):
        if not root:
            return True
        treeParse = []

        def preOrder(node):
            if not node:
                return
            treeParse.append(node.val)
            preOrder(node.left)
            preOrder(node.right)
        preOrder(root)

        print(treeParse)

        newRoot = Node(treeParse[0])

        def constructBST(data):
            current = newRoot
            while current:
                if data > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(data)
                        return
                elif data < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(data)
                        return
                else:
                    if not current.left:
                        current.left = Node(data)
                    elif not current.right:
                        current.right = Node(data)
                    return

        for i in range(1, len(treeParse)):
            constructBST(treeParse[i])

        def compareBST(node1, node2):
            if not node1 and not node2:
                return True
            if ((not node1 and node2) or (not node2 and node1)) or (node1.val != node2.val):
                return False
            return compareBST(node1.left if node1 else None, node2.left if node2 else None) and compareBST(node1.right if node1 else None, node2.right if node2 else None)

        return compareBST(root.left if root else None, newRoot.left if newRoot else None) and compareBST(root.right if root else None, newRoot.right if newRoot else None)

    def findTilt(self, root):
        if not root:
            return 0

        tilt = [0]

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            tilt[0] += abs(left-right)
            return left+right+root.val
        dfs(root)
        return tilt[0]

    def zigzagLevelOrder(self, root):
        traversal = [[root.val]]
        queue = [root]

        def levelOrder():
            nonlocal queue
            while True:
                res = []
                nodes = []
                queue = queue[::-1]
                while len(queue):
                    current = queue.pop()

                    if current.left:
                        res.append(current.left.val)
                        nodes.append(current.left)

                    if current.right:
                        res.append(current.right.val)
                        nodes.append(current.right)

                if len(nodes):
                    for i in nodes:
                        queue.append(i)
                    traversal.append(res)
                else:
                    break

        levelOrder()

        for i in range(1, len(traversal), 2):
            traversal[i] = traversal[i][::-1]
        return traversal

    def rangeSumBST(self, root, low, high):

        total = [0]

        def dfs(node):
            if not node:
                return

            if low <= node.val and node.val <= high:
                total.append(node.val)

            if node and node.left:
                dfs(node.left)
            if node and node.right:
                dfs(node.right)

        dfs(root)
        return sum(total)

    def getTargetCopy(self, original, cloned, target):
        def traverse(node):
            if node is None:
                return None
            if node.val == target.val:
                return node
            left = traverse(node.left)
            if left:
                return left
            right = traverse(node.right)
            if right:
                return right
            return None

        return traverse(cloned)

    def getPathSumII(self, root, targetSum):

        res = []

        def traverse(node, path, targetSum):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right and targetSum == node.val:
                res.append(path)

            if targetSum < 0:
                return

            traverse(node.left, copy.deepcopy(path), targetSum-node.val)
            traverse(node.right, copy.deepcopy(path), targetSum-node.val)
        traverse(root, [], targetSum)
        return res

    def getPathSumIII(self, root, target):

        if not root:
            return 0

        def dfs(node, running_sum):
            nonlocal res

            if not node:
                return

            running_sum += node.val

            if (running_sum-target) in sum_count:
                res += sum_count[(running_sum-target)]

            sum_count[running_sum] += 1
            dfs(node.left, running_sum)
            dfs(node.right, running_sum)
            sum_count[running_sum] -= 1

        res = 0
        sum_count = defaultdict(int)
        sum_count[0] = 1
        dfs(root, 0)
        return res

    def deepestLeavesSum(self, root):
        traversal = [[root.val]]
        queue = [root]

        def levelOrder(node):
            while True:
                res = []
                resNodes = []

                while len(queue):
                    node = queue.pop(0)

                    if node.left:
                        res.append(node.left.val)
                        resNodes.append(node.left)
                    if node.right:
                        res.append(node.right.val)
                        resNodes.append(node.right)

                if len(res):
                    queue.extend(resNodes)
                    traversal.append(res)
                else:
                    break

        levelOrder(root.left)
        levelOrder(root.right)

        return sum(traversal[-1])

    def amountOfTime(self, root, start):

        if not root or (root and not root.left and not root.right):
            return 0

        def convert(node, val, graph):
            if not node:
                return
            graph[node.val] = []

            if val != 0:
                graph[node.val].append(val)

            if node.left:
                graph[node.val].append(node.left.val)

            if node.right:
                graph[node.val].append(node.right.val)

            convert(node.left, node.val, graph)
            convert(node.right, node.val, graph)

            return graph

        graph = convert(root, 0, {})

        print(graph)

        visited = set()
        visited.add(start)

        minutes = -1

        q = [start]

        while len(q):
            size = len(q)
            while size:
                NODE = q.pop(0)
                for i in graph[NODE]:
                    if i not in visited:
                        visited.add(i)
                        q.append(i)
                size -= 1
            minutes += 1
        return minutes

    def maxAncestorDiff(self, root):

        def dfs(node, min_val, max_val):
            if not node:
                return max_val - min_val

            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            left_diff = dfs(node.left, min_val, max_val)
            right_diff = dfs(node.right, min_val, max_val)

            return max(left_diff, right_diff)

        return dfs(root, root.val, root.val)

    def levelOrderBottom(self, root):
        if not root:
            return []

        queue = [root]

        traversal = [[root.val]]

        while True:
            res = []
            nodes = []

            while len(queue):
                node = queue.pop(0)

                if node.left:
                    res.append(node.left.val)
                    nodes.append(node.left)

                if node.right:
                    res.append(node.right.val)
                    nodes.append(node.right)

            if len(res):
                queue.extend(nodes)
                traversal.append(res)
            else:
                break
        return traversal[::-1]

    def bstToGst(self, root):
        keys = []

        def dfs(node):
            if not node:
                return
            keys.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        keys.sort()

        def replaceValues(node):
            if not node:
                return

            index = keys.index(node.val)
            summation = sum(keys[index:])
            node.val = summation

            replaceValues(node.left)
            replaceValues(node.right)
            return

        # ! https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/

    def flatten(self, root):
        if not root:
            return

        traverse = []

        def dfs(root):
            if not root:
                return
            traverse.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)

        N = len(traverse)

        def construct(val, i):
            if i == N-1:
                return None

            node = Node(val)
            node.left = None
            node.right = Node(construct(traverse[i+1], i+1))
            return node

        return construct(traverse[0], 0)

    def pseudoPalindromicPaths(self, root):
        count = defaultdict(int)
        odd = 0

        def dfs(root):
            nonlocal odd
            if not root:
                return 0

            count[root.val] += 1
            odd_change = 1 if count[root.val] % 2 == 1 else -1
            odd += odd_change

            if not root.left and not root.right:
                res = 1 if odd <= 1 else 0
            else:
                res = dfs(root.left)+dfs(root.right)

            odd -= odd_change
            count[root.val] -= 1

            return res

        return dfs(root)

    def bstFromPreorder(self, preorder):
        if not preorder:
            return None

        root = Node(preorder.pop(0))

        def addNode(node, val):
            if not node:
                return
            if val > node.val:
                if node.right:
                    addNode(node.right, val)
                else:
                    node.right = TreeNode(val)
            else:
                if node.left:
                    addNode(node.left, val)
                else:
                    node.left = TreeNode(val)

        while len(preorder):
            self.addNode(root, preorder.pop(0))
        return root

    def connect(self, root):
        if not root:
            return
        queue = [root]
        while True:
            nodes = []
            while len(queue):
                node = queue.pop(0)
                if not queue:
                    node.next = None
                else:
                    node.next = queue[0]
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if not len(nodes):
                break
            else:
                queue.extend(nodes)
        return root

    def sumEvenGrandparent(self, root):
        nodes = []

        def dfs(node):
            if not node:
                return

            if node.val % 2 == 0:
                nodes.append(node)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        res = 0

        while len(nodes):
            node = nodes.pop(0)

            def summation(node, level):
                nonlocal res

                if not node:
                    return

                if level == 2 and node:
                    res += node.val
                    return

                summation(node.left, copy.deepcopy(level+1))
                summation(node.right, copy.deepcopy(level+1))

            summation(node, 0)

        return res

    def maxPathSum(self, root):
        self.maxSum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.maxSum = max(self.maxSum, left+right+node.val)
            return max(left, right)+node.val
        dfs(root)
        return self.maxSum

    def evaluateTree(self, root):

        if not root:
            return False

        if not root.left and not root.right:
            return bool(root.val)

        def evaluate(node):
            if not node:
                return
            if not node.left and not node.right:
                return bool(node.val)
            else:
                if node.val == 2:
                    node.val = bool(evaluate(node.left)) or bool(
                        evaluate(node.right))
                else:
                    node.val = bool(evaluate(node.left)) and bool(
                        evaluate(node.right))
            return node.val

        return evaluate(root)

    def smallestFromLeaf(self, root):

        def dfs(root, cur):
            if not root:
                return
            cur = chr(ord('a')+root.val) + cur
            if root.left and root.right:
                return min(dfs(root.left, cur), dfs(root.right, cur))
            if root.left:
                return dfs(root.left, cur)
            if root.right:
                dfs(root.right, cur)

            return cur
        return dfs(root, "")

    def rightSideView(self, root):
        if not root:
            return
        queue = [root]
        res = [root.val]
        while True:
            childNodes = []
            levelTraverse = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left is not None:
                    childNodes.append(node.left)
                    levelTraverse.append(node.left.val)
                if node.right is not None:
                    childNodes.append(node.right)
                    levelTraverse.append(node.right.val)
            if len(childNodes):
                queue = childNodes
                res.append(levelTraverse[-1])
            else:
                break
        return res

    def reverseOddLevels(self, root):
        if not root:
            return

        queue = []

        level = 1
        while True:
            traversalNodes = []
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    traversalNodes.append(node.left)
                if node.right:
                    traversalNodes.append(node.right)
                if level % 2 != 0:
                    node.left.val, node.right.val = node.right.val, node.left.val
            level += 1
            if len(queue):
                queue.insert(traversalNodes)
            else:
                break
        return root


tree = Tree()

n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)

n1.left.left = Node(4)
# n1.left.right=Node(5)

# n1.right.left = Node(3)
# n1.right.right = Node(4)

tree = Tree()
tree.rightSideView(n1)
# print(tree.sumEvenGrandparent(n1))
# print(tree.pseudoPalindromicPaths(n1))

# print(tree.flatten(n1))

# n1 = Node(1)
# n1.right = Node(2)
# n1.right.right = Node(0)
# n1.right.right.left = Node(3)

# n1.left.right = Node(4)

# n1.left.right.left = Node(9)
# n1.left.right.right = Node(2)

# n1.right.left = Node(10)
# n1.right.right = Node(6)

# print(tree.maxAncestorDiff(n1))
# print(tree.amountOfTime(n1, 3))


# print(tree.getPathSumIII(n1, 1))
# print(tree.deepestLeavesSum(n1))

# n2 = Node(10)
# n2.left = Node(5)
# n2.right = Node(15)
# n2.left.left = Node(3)
# n2.left.right = Node(7)
# n2.right.right = Node(18)


# print(tree.getPathSumII(n1, 18))
# res = tree.getTargetCopy(n1, n2, n1.left.left)
# print(res.val)
# print(tree.rangeSumBST(n1, 7, 15))
# print(tree.zigzagLevelOrder(n1))
# print(tree.checkTree(n1))
# print(tree.levelOrderTraversal(n1))

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

# N1 = Node(2)
# N2 = Node(1)
# N3 = Node(3)
# N4 = Node(3)
# N5 = Node(3)
# N6 = Node(4)
# N7 = Node(4)

# N1.left = N2
# N1.right = N3

# N1.left.left = N4
# N1.left.right = N5

# N1.left.left.left = N6
# N1.left.left.right = N7


# print(tree.isBalanced(N1))
# print(tree.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]))

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
