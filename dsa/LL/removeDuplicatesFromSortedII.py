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
        countMap = {}
        while current:
            countMap[current.val] = countMap.get(current.val, 0) + 1
            current = current.next
        new_node = Node(0)
        ptr = new_node
        for key in countMap.keys():
            if countMap[key] == 1:
                new_node.next = Node(key)
                new_node = new_node.next
        return ptr.next
            
        
node1 = Node(-3)
ll = LinkedList(node1)

ll.append(-1)
ll.append(-1)
ll.append(0)
ll.append(0)
ll.append(0)
ll.append(0)
ll.append(0)
ll.append(2)
new_ll = ll.removeDuplicates()
ll1 = LinkedList(new_ll)
ll1.print_list()