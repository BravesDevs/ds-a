class Solution:
    def removeNthFromEnd(self, node):

        n=1
        while node.next:
            n+=1
            node = node.next
        
        dummy = ListNode(0)
        dummy.next = node
        first = dummy
        second = dummy
        for i in range(n+1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next