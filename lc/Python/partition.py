class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def __init__(self, head=None):
        self.head = head

    def print_list(self, head=None):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def append(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    #! Solved using arrays
    # def partition(self, head, x):
    #     current = self.head
    #     lowLi = []
    #     highLi = []

    #     while current is not None:
    #         if current.data >= x:
    #             highLi.append(current.data)
    #         else:
    #             lowLi.append(current.data)
    #         current = current.next

    #     li = lowLi+highLi

    #     n1 = Node(li[0])

    #     current = n1

    #     for i in range(1, len(li)):
    #         current.next = Node(li[i])
    #         current = current.next
    #     return n1

    # ? Solve using 2 pointer strategy
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head
        n1 = ListNode(0)
        n2 = ListNode(0)
        p1 = n1
        p2 = n2
        current = head
        while current is not None:
            node = ListNode(current.val)
            if current.val < x:
                p1.next = node
                p1 = p1.next
            else:
                p2.next = node
                p2 = p2.next
            current = current.next

        ptr1 = n1.next
        n1 = n1.next

        if ptr1 is not None:
            while ptr1.next is not None:
                ptr1 = ptr1.next
            ptr1.next = n2.next
        return n1 if n1 is not None else n2.next


sln = Solution()
sln.append(2)
# sln.append(4)
# sln.append(3)
# sln.append(2)
# sln.append(5)
sln.append(1)
# sln.print_list()
result = sln.partition(sln, 2)
# sln.print_list(result)
