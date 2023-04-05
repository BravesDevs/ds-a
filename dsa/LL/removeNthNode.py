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
    
    def removeNthNode(self,n):
        length = self.get_length()
        current = self.head
        if(length<=1):
            current = None
            self.head = current
        elif(n == length):
            self.head = current.next
        else:
            pos=0
            while pos<length-(n+1):
                current = current.next
                pos+=1
            current.next=current.next.next


    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next




node1 = Node(1)
ll = LinkedList(node1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.append(5)
ll.removeNthNode(1)
ll.print_list()