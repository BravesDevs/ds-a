import sys
import copy


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Sol:
    # def __init__(self, head=None):
    #     self.head = head

    def print_list(self, head):
        current = head
        # visited = set()
        while current:
            # if current in visited:
            #     break
            # visited.add(current)
            print(current.data)
            current = current.next

    def getLength(self, head):
        print("TRAVERSING THE LINKED_LIST")
        if not head:
            return 0

        length = 1
        current = head.next

        while current:
            current = current.next
            length += 1
        return length

    def swapNodes(self, head, k):
        li = []
        current = head
        while current:
            li.append(current.data)
            current = current.next

        li[len(li)-k], li[k-1] = li[k-1], li[len(li)-k]
        print(li)
        ll = ListNode(0)
        node = ll
        for i in li:
            node.next = ListNode(i)
            node = node.next
        return ll.next


n1 = ListNode(91)
n2 = ListNode(56)
n3 = ListNode(48)
n4 = ListNode(77)
n5 = ListNode(91)
n6 = ListNode(96)
n7 = ListNode(55)
n8 = ListNode(53)
n9 = ListNode(68)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9

sln = Sol()

ll = sln.swapNodes(n1, 7)
print(sln.print_list(ll))
