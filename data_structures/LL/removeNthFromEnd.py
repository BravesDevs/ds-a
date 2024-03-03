class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def printList(self, head):
        if not head:
            return
        ptr = head

        while ptr:
            print(ptr.val)
            ptr = ptr.next
        return

    def removeNthFromEnd(self, head, n):
        if not head:
            return

        ptr = head
        size = 0

        while ptr:
            size += 1
            ptr = ptr.next

        if n < 0 or n > size:
            return
        if n == size:
            head = head.next
        else:
            ptr = head
            for _ in range(size - n - 1):
                ptr = ptr.next
            if ptr.next:
                ptr.next = ptr.next.next
        return head


n1 = ListNode(1)
n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)

n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5


sln = Solution()

ll = sln.removeNthFromEnd(n1, 1)

print(sln.printList(ll))
