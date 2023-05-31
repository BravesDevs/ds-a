import math


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class RootNthNode:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def rootNode(self):
        slow, fast = 1, 1
        res = 0
        ptr = self.head
        i,j=1,1
        while ptr is not None:
            if i==j*j:
                res = j
                j+=1
            i+=1
            ptr = ptr.next
        return res

Node1 = Node(1)
ll = RootNthNode(Node1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)
ll.append(8)
ll.append(9)
ll.append(10)
ll.append(11)
ll.append(12)
ll.append(13)
ll.append(14)
ll.append(15)
ll.append(16)

rootNode = ll.rootNode()
print("Root node: ", rootNode)
