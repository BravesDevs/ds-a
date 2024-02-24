class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution:
    def mergeNodes(self, head):
        ptr1 = head
        ptr2 = head.next
        current = head
        total = 0
        while ptr2:
            if ptr2.val == 0:
                current.next = ListNode(total)
                current = current.next
                total = 0
                ptr1 = ptr2
            else:
                total += ptr2.val
            ptr2 = ptr2.next
        current.next = ListNode(total)

        current.next = None
        head = head.next

        return head

    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


n1 = ListNode(0)
n1.next = ListNode(1)
n1.next.next = ListNode(0)
n1.next.next.next = ListNode(3)
n1.next.next.next.next = ListNode(0)
n1.next.next.next.next.next = ListNode(2)
n1.next.next.next.next.next.next = ListNode(2)
n1.next.next.next.next.next.next.next = ListNode(0)

sln = Solution()
sln.mergeNodes(n1)
