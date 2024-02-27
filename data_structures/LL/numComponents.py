class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head, G):
        if not head:
            return 0

        ptr = head
        li = []
        while ptr:
            li.append(ptr.val)
            ptr = ptr.next

        stack = []
        count = 0
        for i in range(len(li)):
            if li[i] in G:
                if not stack:
                    count += 1
                stack.append(li[i])
            else:
                if stack:
                    stack = []

        return count
