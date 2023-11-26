import math


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def traverseList(self, head):
        current = head

        while current:
            print(current.val)
            current = current.next

    def insertGreatestCommonDivisors(self, head):
        firstPtr = head
        secondPtr = firstPtr.next

        n1 = Node(firstPtr.val)
        ptr = n1

        while secondPtr:
            gcd = math.gcd(firstPtr.val, secondPtr.val)

            ptr.next = Node(gcd)
            ptr.next.next = Node(secondPtr.val)
            ptr = ptr.next.next
            firstPtr = firstPtr.next
            secondPtr = firstPtr.next

        return n1


n1 = Node(18)
n2 = Node(6)
n3 = Node(10)
n4 = Node(3)

n1.next = n2
n2.next = n3
n3.next = n4


sln = Solution()

new_ll = sln.insertGreatestCommonDivisors(n1)

print(sln.traverseList(new_ll))
