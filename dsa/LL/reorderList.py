class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Sol:
    def printList(self, head):
        if not head:
            return

        current = head
        while current:
            print(current.val)
            current = current.next
        return ""

    def reorderList(self, head):
        if not head:
            return

        left = head
        li = []
        liLeft = []
        liRight = []
        count = 0

        while left:
            li.append(left.val)
            left = left.next

        if len(li) % 2 == 0:
            left, right = 0, len(li)-1
            while left < right:
                liLeft.append(li[left])
                liRight.append(li[right])
                left += 1
                right -= 1
        else:
            left, right = 0, len(li)-1
            while left <= right:
                if left == right:
                    liLeft.append(li[left])
                else:
                    liLeft.append(li[left])
                    liRight.append(li[right])
                left += 1
                right -= 1

        n1 = Node(0)
        current = n1
        for i in range(max(len(liLeft), len(liRight))):
            if i < len(liLeft):
                current.next = Node(liLeft[i])
                current = current.next
            if i < len(liRight):
                current.next = Node(liRight[i])
                current = current.next
        return n1.next


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
# n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
# n4.next = n5

sln = Sol()

ll = sln.reorderList(n1)

print(sln.printList(ll))
