from fractions import gcd


class Node:
    def __init__(self, val=None, next=None):
        self.val = data
        self.next = None


class Solution:
    def printList(self, head):
        ptr = head
        while ptr:
            print(ptr.val)
            ptr = ptr.next

    def insertGreatestCommonDivisors(self, head):
        if not head:
            return
        p1 = head
        p2 = p1.next

        while p2:
            node = gcd(p1.val, p2.val)
            node.next = p2
            p1.next = node
            
            p1 = p2
            p2 = p2.next
        return head


node = Node(18)
node.next = Node(6)
node.next.next = Node(10)
node.next.next.next = Node(3)

sln = Solution()
newLL = sln.insertGreatestCommonDivisors(node)

sln.printList(newLL)
