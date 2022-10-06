from array import Array


class Queue:
    CAPACITY = 10

    def __init__(self, capacity=CAPACITY):
        self.capacity = capacity
        self.arr = Array(self.capacity)
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self):
        raise NotImplemented

    def peek(self):
        if self.is_empty():
            raise Exception("queue is empty.")
        return self.arr[self.front]

    def __len__(self):
        raise NotImplemented

    def __str__(self):
        return str(self.arr)

    def __iter__(self):
        # pos = 0
        # while pos < len(self):
        #     yield self.arr[pos]
        #     pos += 1
        tmp = self.front
        while self.arr[self.front] != None:
            yield self.arr[self.front]
            self.front = (self.front + 1) % 8
        self.front = tmp
        # return iter(self.arr[self.front])

    def enqueue(self, elem):
        self.rear = (self.rear + 1) % 8
        self.arr[self.rear] = elem

        if self.front == -1:
            self.front += 1

    def dequeue(self):
        self.front = self.front % 8
        self.arr[self.front] = None
        self.front += 1

        if self.front == self.rear:
            self.arr[self.front] = None
            self.front = self.rear = -1


if __name__ == "__main__":
    N = 8
    queue = Queue(N)
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    queue.enqueue("D")
    print(queue)
    print("Peek:", queue.peek())
    queue.dequeue()
    print("Peek:", queue.peek())
    queue.dequeue()
    print(queue)
    queue.enqueue("E")
    queue.enqueue("F")
    queue.enqueue("G")
    queue.enqueue("H")
    queue.enqueue("I")
    queue.enqueue("J")
    print(queue)
    queue.dequeue()
    print(queue)
    for i in queue:
        print("Element:", i)
    print("Peek:", queue.peek())
    while not queue.is_empty():
        queue.dequeue()
    print(queue)