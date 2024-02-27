class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head):
        if not head:
            return

        ptr = head
        li = []
        while ptr:
            li.append(ptr.val)
            ptr = ptr.next

        stack = []

        for i in range(len(li)):
            while stack and li[i] > li[stack[-1]]:
                li[stack.pop()] = li[i]
            stack.append(i)

        while stack:
            li[stack.pop()] = 0

        return li


n1 = ListNode(2)
n2 = ListNode(1)
n3 = ListNode(5)

n1.next = n2
n2.next = n3

sln = Solution()
print(sln.nextLargerNodes(n1))
