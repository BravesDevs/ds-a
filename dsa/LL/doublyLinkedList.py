class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.initial=head
    def append(self,data):
        new_node = Node(data)

        if self.head:
            current = self.head
            while current.next:
                current = current.next
            
            current.next = new_node
            new_node.prev = current
        else:
            self.head = new_node
            new_node.prev = self.head

    def get_length(self):
        count=0
        current = self.head
        while current.next:
            count+=1
            current=current.next
        return count

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def peek_previous(self,node_location):
        length = self.get_length()
        if(node_location>length):
            print("Invalid location")
            return
        else:
            current = self.head
            count = 0
            while count < node_location:
                current = current.next
                count=count+1

            print("Current Node:", current.data)
            print("Prev Node:",current.prev.data)
           

    def insert_At_position(self,data,location):
        length = self.get_length()
        initial=self.head if self.head else None
        if(location>length+1):
            print("Invalid Operation")
            return
        else:
            new_node = Node(data)
            current = self.head
            if(location<1):
                new_node.next=current
                new_node.prev=current.prev
                current.prev=new_node
                self.head=initial

            elif location>=1 and location < length:
                count=0
                while count<location:
                    current=current.next
                    count+=1
                
                new_node.next = current
                new_node.prev=current.prev
                current.prev.next = new_node
                current.prev=new_node
                self.head=initial
            
            elif location>length:
                initial = self.head
                while current.next:
                    current=current.next
                new_node.next=current.next
                new_node.prev=current
                current.next=new_node
                self.head=initial

    def delete_At_position(self,location):
        length = self.get_length()
        if(location>length):
            print("Invalid location")
            return
        else:
            current = self.head
            if location<1:
                self.head=current.next
                self.head.prev=None

            elif location==length:
                count=0

                while count<length:
                    current=current.next
                    count=count+1

                current.prev.next=None
                current.next=None
                self.head=self.initial
            
            else:
                count=0
                while count<location:
                    current=current.next
                    count=count+1
                current.prev.next=current.next
                current.next.prev = current.prev
                current=None
                self.head = self.initial
    
    def traverse_bi_directional(self):
        print("None")
        print("⬇️⬆️")
        if(self.head):
            print(self.head.data)
            print("⬇️⬆️")
            while(self.head.next is not None):
                self.head = self.head.next
                print(self.head.data)
                print("⬇️⬆️")
                
            while(self.head.prev):
                self.head=self.head.prev
                print(self.head.data)
                print("⬇️⬆️")
        print("None")

node1 = Node(1)

ll = DoublyLinkedList(node1)
ll.append(2)
ll.append(3)
ll.append(4)
# print("Peeking the data of prev node")
# ll.peek_previous(3)
# print("Inserting at beginning")
# ll.insert_At_position(2,1)
# ll.insert_At_position(6,5)
# ll.delete_At_position(3)
# print("Print the linked list")
# ll.print_list()
print("Printing the list in bi-direction")
ll.traverse_bi_directional()
