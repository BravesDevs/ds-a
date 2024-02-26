from collections import deque


class Q:
    def __init__(self):
        self.q = deque()

    def enQ(self, element):
        self.q.appendleft(element)

    def deQ(self, element):
        return self.q.pop()

    def is_empty(self, element):
        return len(self.q) == 0

    def size(self):
        return len(self.q)
