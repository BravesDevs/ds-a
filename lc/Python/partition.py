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


sln = Solution()
sln.append(1)
sln.append(4)
sln.append(3)
sln.append(2)
sln.append(5)
sln.append(2)
# sln.print_list()
result = sln.partition(sln, 3)
sln.print_list(result)
