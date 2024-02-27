class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.child = None


class Solution:
    def flatten(self, head):

        if not head:
            return None

        li = []

        def dfs(listNode):
            if not listNode:
                return
            li.append(listNode)
            if listNode.child:
                dfs(listNode.child)
                listNode.child = None
            dfs(listNode.next)

        dfs(head)

        node = li.pop(0)
        ptr = node
        prev = None
        while len(li):
            ptr.next = li.pop(0)
            ptr.next.prev = ptr
            prev = ptr
            ptr = ptr.next

        return node


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node1.prev = None
node1.child = node3

node2.prev = node1
node2.next = None
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node6 = Node(6)
# node7 = Node(7)
# node8 = Node(8)
# node9 = Node(9)
# node10 = Node(10)
# node11 = Node(11)
# node12 = Node(12)


# node1.prev = None
# node1.next = node2

# node2.prev = node1
# node2.next = node3

# node3.next = node4
# node3.child = node7
# node3.prev = node2

# node4.next = node5
# node4.prev = node3

# node5.next = node6
# node5.prev = node4

# node7.next = node8
# node7.prev = None

# node8.next = node9
# node8.prev = node7
# node8.child = node11

# node9.next = node10
# node9.prev = node8

# node10.next = None
# node10.prev = node9

# node11.prev = None
# node11.next = node12

# node12.next = None
# node12.prev = node11


sln = Solution()

print(sln.flatten(node1))
