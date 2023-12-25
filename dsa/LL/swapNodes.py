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
        first = head
        last = head
        count = 1

        length = self.getLength(head)

        while True:
            if count < k:
                first = first.next
            if count <= length-k:
                last = last.next
            else:
                break
            count += 1
        print("============================")
        print(first.data)
        print(last.data)
        print("============================")
        if first == last:
            return head

        current = head

        while current.next != first:
            current = current.next

        tempLast = copy.deepcopy(last)

        last.next = first.next
        current.next = last
        current = current.next
        while current.next != last:
            current = current.next
        first.next = tempLast.next
        current.next = first

        return head


n1 = ListNode(1)
n2 = ListNode(2)
# n3 = ListNode(6)
# n4 = ListNode(6)
# n5 = ListNode(7)
# n6 = ListNode(8)
# n7 = ListNode(3)
# n8 = ListNode(0)
# n9 = ListNode(9)
# n10 = ListNode(5)

n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = n7
# n7.next = n8
# n8.next = n9
# n9.next = n10

sln = Sol()

ll = sln.swapNodes(n1, 1)
print(sln.print_list(ll))
