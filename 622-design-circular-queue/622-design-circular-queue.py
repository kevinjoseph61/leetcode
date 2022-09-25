class MyCircularQueue:

    def __init__(self, k: int):
        self.lst = [0]*k
        self.max_size = k
        self.size = 0
        self.front = self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.rear == -1 and self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.lst[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.front = (self.front + 1) % self.max_size
        if self.size == 0:
            self.rear = self.front = -1
        return True

    def Front(self) -> int:
        return self.lst[self.front] if self.front!=-1 else -1

    def Rear(self) -> int:
        return self.lst[self.rear] if self.rear!=-1 else -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.size == self.max_size:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()