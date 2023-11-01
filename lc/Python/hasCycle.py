import math


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.visited = []

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

    def hasCycle(self):
        current = self.head

        while current is not None:
            if current in self.visited:
                return True
            self.visited.append(current)
            current = current.next

        return False

    def isPalindrome(self):
        current = self.head

        stack = []

        length = self.get_length()

        mid = length // 2

        for i in range(mid):
            stack.append(current.data)
            current = current.next

        if length % 2 == 1:
            current = current.next

        while current is not None:
            if current.data != stack.pop():
                return False
            current = current.next

        return True

    def reverseLinkedList(self):
        prev = None
        current = self.head

        while current is not None:
            nextNode = current.next

            current.next = prev

            prev = current

            current = nextNode

        self.head = prev

    def deleteDuplicates(self):
        currPtr = self.head
        nextPtr = currPtr.next

        while nextPtr is not None:
            if currPtr.data == nextPtr.data:
                currPtr.next = nextPtr.next
            else:
                currPtr = nextPtr
            nextPtr = nextPtr.next


n1 = Node(1)
n2 = Node(1)
n3 = Node(2)
n4 = Node(3)
n5 = Node(3)
n6 = Node(3)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = None

ll = LinkedList(n1)
# ll.reverseLinkedList()
ll.deleteDuplicates()
# print(ll.isPalindrome())
ll.print_list()
