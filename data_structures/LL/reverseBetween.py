# LC 92: Reverse Linked List II

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = ListNode(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def print_list(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next

    def get_length(self, head=None):
        if head is None:
            count = 1
            current = self.head
            while current.next:
                count += 1
                current = current.next
            return count
        count = 1
        current = self.head
        while current.next:
            count += 1
            current = current.next
        return count

    def reverseLL(self, head):
        prev = None
        current = head
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        head = prev
        return head

    def reverseBetween(self, head, left, right):
        if left == right:
            return head

        if left == 1 and right == self.get_length(head):
            return self.reverseLL(head)

        prevPart = None
        leftPtr = head

        count = 1

        while count < left:
            prevPart = leftPtr
            leftPtr = leftPtr.next
            count += 1

        node = ListNode(leftPtr.val)
        current = node

        while count < right:
            current.next = ListNode(leftPtr.next.val)
            leftPtr = leftPtr.next
            current = current.next
            count += 1
        nextPart = leftPtr.next

        reversedLLHead = self.reverseLL(node)
        current = reversedLLHead

        if prevPart is not None:
            prevPart.next = reversedLLHead
        
        head = head if prevPart is not None else reversedLLHead

        if nextPart is not None:
            while current is not None and current.next != None:
                current = current.next
            current.next = nextPart

        return head


node1 = ListNode(1)
node1.next = ListNode(2)
# node1.next.next = ListNode(3)
# node1.next.next.next = ListNode(4)
# node1.next.next.next.next = ListNode(5)

ll = Solution(node1)

result = ll.reverseBetween(node1, 1, 2)
ll.print_list(result)
# ll.print_list()
