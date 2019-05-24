class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        if self.current == (self.capacity - 1):
            self.current = 0
        else:
            self.current += 1

    def get(self):
        arr = []
        for i in self.storage:
            if i != None:
                arr.append(i)
        return arr

ring = RingBuffer(3)
print(len(ring.storage))  # Length = 3

ring.append('a')
ring.append('b')
print(len(ring.storage))  # Still 3
print(ring.get())  # ['a', 'b']

ring.append('c')
print(len(ring.storage))  # 3
print(ring.get())  # , ['a', 'b', 'c'])

ring.append('d')
print(len(ring.storage))  # 3
print(ring.get())  # , ['d', 'b', 'c'])

ring.append('e')
ring.append('f')
print(len(ring.storage))  # 3)
print(ring.get())  # , ['d', 'e', 'f')

