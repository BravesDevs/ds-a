class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, head = None, length=None):
        self.head = head
        self.length = length

    def get_length(self):
        count=0
        current = self.head
        while current.next:
            count+=1
            current=current.next
        return count
    
    def push(self,data):
        stack_length = self.get_length()
        if(stack_length<self.length-1):
            new_node = Node(data)
            if self.head:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
            else:
                self.head = new_node
            return
        else:
            print("Stack Overflow")
            return

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def pop(self):
        count = 1
        current = self.head
        while count<self.get_length():
            current=current.next
            count=count+1
        print("Popped:",current.next.data)
        current.next = None            
    
    def peek(self):
        count=0
        current=self.head
        while count<self.get_length():
            current=current.next
            count=count+1
        print("Top",current.data)
    
    def nthNodeFromEnd(self,node):
        current = self.head
        length = self.get_length()-node
        count = 1
        while count<length+1:
            current=current.next
            count=count+1
        print("Nth Node", current.data)

node1 = Node(1)
ll = Stack(node1,5)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.peek()
# ll.pop()
# ll.pop()
# ll.pop()
# ll.peek()

# ll.push(7)
ll.nthNodeFromEnd(1)
ll.print_list()
