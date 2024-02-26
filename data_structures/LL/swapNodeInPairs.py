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

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def get_length(self):
        count = 1
        current = self.head
        while current.next:
            count += 1
            current = current.next
        return count 
    
    def swap_node_in_pair(self):
        current = self.head
        length = self.get_length()
        if length <= 1:
            return
        elif length == 2:
            self.head = current.next
            current.next = current.next.next
            self.head.next = current
        else:
            self.head = current.next
            current.next = current.next.next
            self.head.next = current
            prev = current
            current = current.next
            while current and current.next:
                temp = current.next
                current.next = current.next.next
                temp.next = current
                prev.next = temp
                prev = current
                current = current.next
                

node1 = Node(1)

ll = LinkedList(node1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
# ll.append(6)
ll.swap_node_in_pair()

ll.print_list()
