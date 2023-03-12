class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self,data):
        current=self.head
        new_node = Node(data)
        while current.next is not None and current.next!=self.head:
            current=current.next
        
        new_node.next=self.head
        new_node.prev=current
        current.next = new_node
    
    def get_length(self):
        count=0
        current = self.head
        while current.next is not None and current.next!=self.head:
            count+=1
            current=current.next
        return count

    def print_ll(self):
        current=self.head
        print(current.data)
        while current.next is not None and current.next!=self.head:
            current=current.next
            print(current.data)

    def insert_at_position(self,data,location):
        length = self.get_length()

        if location > length+1:
            print("Invalid Location")
            return
        
        elif location<1:
            new_node = Node(data)

            current = self.head 
            while current.next is not None and current.next!=self.head:
                current = current.next
            
            new_node.next = self.head
            self.head.prev=new_node

            new_node.prev=current
            current.next=new_node
            self.head = new_node

        elif location==length:
            self.append(data)

        else:
            count=0
            current=self.head
            while count<location:
                current=current.next
                count=count+1
            
            print("Pointer:",current.data)
            new_node = Node(data)
            current.prev.next = new_node
            new_node.prev = current.prev
            current.prev = new_node
            new_node.next = current

node1 = Node(1)
ll = CircularLinkedList(node1)
ll.append(2)
ll.append(4)
ll.append(5)
ll.insert_at_position(0,0)
ll.insert_at_position(3,3)
ll.insert_at_position(6,6)
ll.print_ll()
        