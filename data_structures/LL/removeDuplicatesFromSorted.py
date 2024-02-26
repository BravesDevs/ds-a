class Node:
    def __init__(self, data):
        self.val = data
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

    def print_list(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next
    
    def removeDuplicates(self):
        current = self.head
        
        while current is not None:
            ptr = current.next

            while ptr is not None and current.val == ptr.val:
                ptr = ptr.next

            current.next = ptr
            current = current.next

node1 = Node(1)
ll = LinkedList(node1)

# ll.append(1)
# ll.append(2)
# ll.append(3)
# # ll.append(3)
ll.removeDuplicates()
ll.print_list()