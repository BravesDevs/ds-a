
class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = [None] * k
        self.k = k
        self.rear = self.head = -1

    def enQueue(self, value):
        if self.isFull():
            return False

        if self.rear == -1:
            self.rear = self.head = 0
        else:
            self.rear = (self.rear + 1) % len(self.queue)

        self.queue[self.rear] = value
        return True

    def deQueue(self):
        if self.isEmpty():
            return False

        if self.head == self.rear:
            self.head = self.rear = -1
        else:
            self.head = (self.head + 1) % len(self.queue)
        return True

    def Front(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[self.head]

    def Rear(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        return len(self.queue) == 0 or self.head == -1

    def isFull(self):
        return (self.rear+1) % len(self.queue) == self.head


# Your MyCircularQueue object will be instantiated and called as such:

obj = MyCircularQueue(4)
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.enQueue(4))
print(obj.deQueue())
print(obj.enQueue(5))
# print(obj.isFull())
# print(obj.enQ~ueue(4))