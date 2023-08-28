class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self, head=None, root=None):
        self.head = head
        self.root = root
        self.traversePath = []

    def print_list(self, head=None):
        current = self.head
        while current is not None:
            print(current.val)
            current = current.next

    def append(self, val):
        new_node = ListNode(val)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def addNode(self, data):
        new_node = TreeNode(data)
        if self.root:
            current = self.root

            while current:
                if data > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = new_node
                        return self.root
                else:
                    if current.left:
                        current = current.left
                    else:
                        current.left = new_node
                        return self.root
        else:
            self.root = new_node

        return self.root


    def sortedListToBST(self, head):
        current = self.head
        elements = []
        count = 0

        # Finding the length of the linkedList
        while current is not None:
            elements.append(current.val)
            count += 1
            current = current.next

        # Finding the mid node
        mid = [elements[count//2]]
        # print(mid)
        leftPass = elements[:count//2][::-1]
        # print("Left: ",leftPass)
        rightPass = elements[(count//2)+1:]
        # print("Right: ",rightPass)

        orderElements = mid+leftPass+rightPass
        treeNode=None
        for i in orderElements:
            treeNode = self.addNode(i)
        return treeNode
        
    def levelOrderTraversal(self, node):
        self.traversePath = []
        if node is None:
            return
        queue = [node]
        while len(queue) > 0:
            current = queue.pop(0)
            self.traversePath.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        print(self.traversePath)





sln = Solution()
sln.append(-10)
sln.append(-3)
sln.append(0)
sln.append(5)
sln.append(9)
# sln.print_list()
treeNode = sln.sortedListToBST(sln)

sln.levelOrderTraversal(treeNode)

