# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        leftL = ListNode(0)
        rightL = ListNode(0)
        
        pL = leftL
        pR = rightL
        ptr = head

        while ptr:
            if ptr.val<x:
                pL.next = ListNode(ptr.val)
                pL = pL.next
            else:
                pR.next = ListNode(ptr.val)
                pR = pR.next
            ptr = ptr.next
        pL.next = rightL.next

        return leftL.next
