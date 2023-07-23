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


# class Tree:
#     def __init__(self, root=None):
#         self.root = root
#         self.traversePath = []
#         # self.difference= int('inf')

#     def addNode(self, data):
#         new_node = Node(data)
#         if self.root:
#             current = self.root

#             while current:
#                 if data > current.val:
#                     if current.right:
#                         current = current.right
#                     else:
#                         current.right = new_node
#                         return
#                 else:
#                     if current.left:
#                         current = current.left
#                     else:
#                         current.left = new_node
#                         return
#         else:
#             self.root = new_node

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

#     def levelOrderTraversal(self, node):
#         self.traversePath = []
#         if node is None:
#             return
#         queue = [node]
#         while len(queue) > 0:
#             current = queue.pop(0)
#             self.traversePath.append(current.val)
#             if current.left:
#                 queue.append(current.left)
#             if current.right:
#                 queue.append(current.right)

#         return self.traversePath

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


tree = Tree()
tree.create_node("1","1")
tree.create_node("2","2",parent="1")
tree.create_node("3","3",parent="1")
tree.create_node("4","4",parent="2")
tree.create_node("5","5",parent="2")

tree.show()
# n1 = Node(1)
# n1.left = Node(2)
# n1.right = Node(3)
# n1.left.left = Node(4)
# n1.left.right = Node(5)


tree = Tree(n1)

result = tree.minDepth(tree.root)
print("Result: ", result)

# result = tree.minimumAbsoluteDifference()
# print(result)

# n1 = Node(1)
# tree = Tree(n1)
# tree.addNode(0)
# tree.addNode(48)
# tree.addNode(12)
# tree.addNode(49)

# pre_order = tree.preOrderTraversal(tree.root)
# in_order = tree.inOrderTraversal(tree.root)
# post_order = tree.postOrderTraversal(tree.root)
# level_order = tree.levelOrderTraversal(tree.root)

# print("Pre-order: ",pre_order)
# print("In-order: ",in_order)
# print("Post-order: ", post_order)
# print("Level-order: ", level_order)
