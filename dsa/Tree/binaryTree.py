# A Python class that represents
# an individual node in a Binary Tree
import math
from treelib import Node, Tree
tree = Tree()


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.count = 1
        self.countLi = []


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

    def isSame(self, p, q):
        def traverseTree(p, q):
            if p is None and q is None:
                return True

            if ((p and not q) or (q and not p)) or (p.val != q.val):
                return False

            return traverseTree(p.left, q.left) and traverseTree(p.right, q.right)

        return traverseTree(p, q)

    def pathSum(self, root, target):
        def countVal(node, count):
            if node is None:
                return False

            count += node.val

            if count == target:
                return True
            return countVal(node.left, count) or countVal(node.right, count)

        return countVal(root, 0)

    # def treeTrace(self,node):
    #     mapTree = {}
    #     def trace(node):
    #         if node is None:
    #             return
    #         li=[]
    #         if node.left is not None:
    #             li.append(node.left.val)
    #         if node.right is not None:
    #             li.append(node.right.val)

    #         mapTree[node.val] = li
    #         trace(node.left)
    #         trace(node.right)

    #     trace(node)

        # print(mapTree)

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

n1 = Node(5)
n2 = Node(4)
n3 = Node(8)
n4 = Node(11)
n5 = Node(13)
n6 = Node(4)
n7 = Node(7)
n8 = Node(2)
n9 = Node(1)


n1.left = n2  # 4

n1.right = n3  # 8

n1.left.left = n4  # 11

n1.left.left.left = n7  # 7

n1.left.left.right = n8  # 2

n1.right.left = n5  # 13

n1.right.right = n6  # 4

n1.right.right.right = n9  # 1

# tree = Tree(n1)
# tree.addNode(9)
# tree.addNode(20)
# tree.addNode(15)
# tree.addNode(7)
tree = Tree(n1)
# print(tree.minimumLevelBinaryTree(tree.root))
# print(tree.isSame(n1, n4))
print(tree.mapTree(n1))
# print(tree.pathSum(n1, 22))
# tree.treeTrace(tree.root)
# pre_order = tree.preOrderTraversal(tree.root)
# in_order = tree.inOrderTraversal(tree.root)
# post_order = tree.postOrderTraversal(tree.root)
# level_order = tree.levelOrderTraversal(tree.root)

# print("Pre-order: ",pre_order)
# print("In-order: ",in_order)
# print("Post-order: ", post_order)
# print("Level-order: ", level_order)
