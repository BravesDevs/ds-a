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

    def findKthNodeFromEnd(self,k):
        length = self.get_length() + 1
        if k>length:
            print("Unexpected k")
            return
        else:
            hashMap = self.mapInHashTable()
            print("Element",hashMap[length-(k+1)].data)           

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def mapInHashTable(self):
        pos=1
        current = self.head
        hashTable = {}
        while current:
            hashTable[pos] = current
            current = current.next
            pos+=1
        return hashTable

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
        
    def reverseList(self):
        prev = None
        curr = self.head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        return
            
        
            

            
    

e1 = Node(9)

ll = LinkedList(e1)

ll.append(8)
ll.append(7)
ll.append(6)
ll.append(5)
ll.append(4)
ll.reverseList()
ll.print_list()
# hashMap = ll.mapInHashTable()

# ll.findKthNodeFromEnd(2)
