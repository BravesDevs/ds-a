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

    def insert_At_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def get_length(self):
        count=0
        current = self.head
        while current.next:
            count+=1
            current=current.next
        return count

    def insert_At_position(self,data,pos):
        if pos > self.get_length():
            print("Unexpected position")
            return
        if pos<1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            count = 0
            current = self.head
            while count < pos-1:
                current=current.next
                count+=1
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node

    
    def delete_At_position(self,pos):
        if pos > self.get_length():
            print("Unexpected position")
        elif pos<1:
            self.head = self.head.next
        else:
            count = 0
            current=self.head

            while count<pos-1:
                current = current.next
                count+=1
            current.next = current.next.next
            
        
            

            
    

e1 = Node(1)

ll = LinkedList(e1)

ll.append(2)
ll.append(3)
ll.append(4)
# ll.insert_At_beginning(5)
ll.delete_At_position(1)
# ll.insert_At_position(40,0)

ll.print_list()
