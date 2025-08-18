# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        N = 1      
        ptr = head
        while ptr.next:
            ptr=ptr.next
            N+=1
        k=k%N
        if k==0:
            return head
        curr = head
        for i in range(N-k-1):
            curr=curr.next
        newHead = curr.next
        curr.next = None
        ptr.next = head
        return newHead




    

head = ListNode(0, ListNode(1, ListNode(2,None)))
sln = Solution()
print(sln.rotateRight(head, 2))