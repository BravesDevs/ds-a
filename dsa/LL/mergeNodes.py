class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution:
    def mergeNodes(self, head):
        if head is None:
            return head
        current = head

        res = []
        total = 0

        while current:
            if current.val == 0 and total > 0:
                res.append(total)
                total = 0
            else:
                total += current.val
            current = current.next
        if total > 0:
            res.append(total)

        current = head
        current.val = res.pop(0)
        current.next = None

        while len(res):
            current.next = ListNode(res.pop(0))
            current = current.next
        return head


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
