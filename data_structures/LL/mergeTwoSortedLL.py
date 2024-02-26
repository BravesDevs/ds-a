class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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
        return self.head
    
    def get_length(self):
        count=1
        current = self.head
        while current.next:
            count+=1
            current=current.next
        return count

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

class Solution:
    def __init__(self, ll1,ll2):
        self.ll1 = ll1
        self.ll2 = ll2
    
    def mergeTwoSortedLists(self):
        ptr1 = self.ll1.head
        ptr2 = self.ll2.head
        new_node = Node(0)
        node_ptr = new_node
        while ptr1 is not None or ptr2 is not None:
            print("Inside while")
            if ptr1 is not None and ptr1.data>ptr2.data:
                node_ptr.next = Node(ptr1.data)
                ptr1=ptr1.next
            elif ptr2 is not None and ptr2.data>ptr1.data:
                node_ptr.next = Node(ptr2.data)
                ptr2=ptr2.next
            node_ptr = node_ptr.next
        return new_node.next



node1 = Node(1)
node2 = Node(4)
ll1 = LinkedList(node1)
ll2 = LinkedList(node2)

ll1.append(2)
ll1.append(7)

ll2.append(5)
ll2.append(6)

solution = Solution(ll1,ll2)
newLL = solution.mergeTwoSortedLists()