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
            return hashMap[length-(k+1)].data           

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

    def get_length_from_one(self):
        count=1
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
    
    def removeNthNodeFromEnd(self,n):
        hashMap = self.mapInHashTable()
        length = self.get_length_from_one()
        
        hashMap[length-(n-1)-1].next = hashMap[length-(n-1)-1].next.next
        hashMap[length-(n-1)].next = None
        return

class Solution:
    def __init__(self, ll1,ll2):
        self.ll1 = ll1
        self.ll2 = ll2
    
    def addTwoNumbers(self):
        ptr1 = self.ll1.head
        ptr2 = self.ll2.head
        numLi = []
        carry = 0
        while ptr1 is not None or ptr2 is not None:
            if ptr1 is not None:
                num1 = ptr1.data
                ptr1 = ptr1.next
            else:
                num1 = 0
            if ptr2 is not None:
                num2 = ptr2.data
                ptr2 = ptr2.next
            else:
                num2 = 0
            sum = num1 + num2 + carry
            carry = sum//10
            numLi.append(sum%10)
        if carry>0:
            numLi.append(carry)
        

# Remove nth Node from the end of list
node1 = Node(1)
ll = LinkedList(node1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.append(5)

ll.removeNthNodeFromEnd(1)
ll.print_list()
            
# linkNode1 = Node(5)
# linkNode2 = Node(2)
# ll1 = LinkedList(linkNode1)
# ll2 = LinkedList(linkNode2)

# ll1.append(6)
# ll1.append(4)

# ll2.append(4)
# ll2.append(3)

# slns = Solution(ll1,ll2)

# slns.addTwoNumbers()

# e1 = Node(9)

# ll = LinkedList(e1)

# ll.append(8)
# ll.append(7)
# ll.append(6)
# ll.append(5)
# ll.append(4)
# ll.reverseList()
# ll.print_list()
# hashMap = ll.mapInHashTable()

# ll.findKthNodeFromEnd(2)