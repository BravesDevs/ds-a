class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution:

    def print_list(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next
        return

    def removeNodes(self, head):
        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next
        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next
        stack = stack[::-1]

        localMax = stack[0]

        for i in range(1, len(stack)):
            if stack[i] < localMax:
                stack[i] = None
            else:
                localMax = stack[i]
        stack = [x for x in stack if x is not None]
        head.val = stack.pop(-1)
        current = head
        current.next = None
        while len(stack):
            current.next = ListNode(stack.pop(-1))
            current = current.next
        return head


sln = Solution()
n1 = ListNode(5)
n1.next = ListNode(3)
n1.next.next = ListNode(13)
n1.next.next.next = ListNode(3)
n1.next.next.next.next = ListNode(8)
ll = sln.removeNodes(n1)
print(sln.print_list(ll))
