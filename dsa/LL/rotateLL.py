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

    
    def rotateList(self,k):
        length = self.get_length()

        if length<=1 or k==length or k==0 or k%length==0:
            return self.head
        else:

            k = k % length if k > length else k
            current = self.head
            count=1

            while count<=length-(k+1):
                current=current.next
                count+=1
            
            detach_list = current.next
            current.next=None
            init = detach_list
            ptr = detach_list
            
            while ptr.next is not None:
                ptr=ptr.next
            ptr.next=self.head            
            self.head=init
            return self.head

e1 = Node(1)
ll = LinkedList(e1)
ll.append(2)
ll.append(2)
ll.append(4)
ll.append(5)
ll.rotateList(11)
ll.print_list()
