class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        ptr = self.head

        for _ in range(index):
            ptr = ptr.next
        return ptr.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        newNode = ListNode(val)
        if index <= 0:
            newNode.next = self.head
            self.head = newNode
        else:
            ptr = self.head

            for _ in range(index-1):
                ptr = ptr.next

            temp = ptr.next
            ptr.next = newNode
            newNode.next = temp
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        current = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(index-1):
                current = current.next

            current.next = current.next.next
        self.size -= 1
