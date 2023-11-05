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

    def levelOrderTraversal(self, node):
        self.traversePath = [[node.val]]
        queue = [node]

        while True:
            res = []
            resNodes = []

            while len(queue)>0:
                current = queue.pop()
                if current.left is not None:
                    res.append(current.left.val)
                    resNodes.append(current.left)
                if current.right is not None:
                    res.append(current.right.val)
                    resNodes.append(current.right)
            if len(resNodes)>0:
                for i in resNodes[::-1]:
                    queue.append(i)
                self.traversePath.append(res)
            else:
                break
        
        return [sum(x)/len(x) for x in self.traversePath]


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

n1 = Node(3)
n2 = Node(9)
n3 = Node(20)
n4 = Node(15)
n5 = Node(7)


n1.left = n2
n1.right = n3
n1.left.left=n4
n1.left.right=n5

# tree = Tree(n1)
# tree.addNode(9)
# tree.addNode(20)
# tree.addNode(15)
# tree.addNode(7)
tree = Tree(n1)

# pre_order = tree.preOrderTraversal(tree.root)
# in_order = tree.inOrderTraversal(tree.root)
# post_order = tree.postOrderTraversal(tree.root)
level_order = tree.levelOrderTraversal(tree.root)

# print("Pre-order: ",pre_order)
# print("In-order: ",in_order)
# print("Post-order: ", post_order)
print("Level-order: ", level_order)
