# A Python class that represents
# an individual node in a Binary Tree

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
    
    def minimumAbsoluteDifference(self):
        traversal = self.inOrderTraversal(self.root)
        diff = max(traversal)+1
        for i in range(len(traversal)-1):
            diff=min(diff, abs(traversal[i]-traversal[i+1]))
        return diff



    def preOrderTraversal(self, node):
        if node is None:
            return
        self.traversePath.append(node.val)
        self.preOrderTraversal(node.left)
        self.preOrderTraversal(node.right)

        return self.traversePath

    def inOrderTraversal(self, node):
        if node is None:
            return
        self.inOrderTraversal(node.left)
        self.traversePath.append(node.val)
        self.inOrderTraversal(node.right)

        return self.traversePath

    def postOrderTraversal(self, node):
        if node is None:
            return
        self.postOrderTraversal(node.left)
        self.postOrderTraversal(node.right)
        self.traversePath.append(node.val)

        return self.traversePath


# n1 = Node(5)
# tree = Tree(n1)
# tree.addNode(3)
# tree.addNode(7)
# tree.addNode(2)
# tree.addNode(4)
# tree.addNode(6)
# tree.addNode(8)

n1 = Node(4)
tree = Tree(n1)
tree.addNode(2)
tree.addNode(6)
tree.addNode(1)
tree.addNode(3)

result = tree.minimumAbsoluteDifference()
print(result)

# n1 = Node(1)
# tree = Tree(n1)
# tree.addNode(0)
# tree.addNode(48)
# tree.addNode(12)
# tree.addNode(49)

# pre_order = tree.preOrderTraversal(tree.root)
in_order = tree.inOrderTraversal(tree.root)
# post_order = tree.postOrderTraversal(tree.root)

# print("Pre-order: ",pre_order)
print("In-order: ",in_order)
# print("Post-order: ", post_order)
