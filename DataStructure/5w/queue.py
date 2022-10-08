from array import Array


class Queue:
    CAPACITY = 10

    def __init__(self, capacity=CAPACITY):
        self.arr = Array(capacity)
        self.capacity = capacity
        self.front = self.rear = -1

    def is_full(self):
        return self.rear - self.front == self.capacity - 1

    def is_empty(self):
        return self.front == self.rear == -1

    def enqueue(self, elem):
        if self.is_full():
            raise Exception("Queue is full")

        self.rear += 1
        self.arr[self.rear] = elem

        if self.front == -1:
            self.front = 0

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        self.arr[self.front] = None
        self.front += 1

        if self.front > self.rear:
            self.front = self.rear = -1

    def peek(self):
        return self.arr[self.front]

    def __len__(self):
        if self.rear == self.front == -1:
            return 0
        return self.rear - self.front + 1

    def __iter__(self):
        pos = 0
        while pos < len(self):
            yield self.arr[pos]
            pos += 1

    def __str__(self):
        return str(self.arr)


if __name__ == "__main__":
    N = 4
    queue = Queue(N)
    print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    print(len(queue), queue)
    queue.enqueue(4)
    print(len(queue), queue)

# if __name__ == "__main__":
#     N = 5
#     q = Queue(N)
#     print("Length:", len(q))
#     print("Empty:", q.is_empty())
#     print("Enqueue 1-", N)
#
#     for i in range(1, N + 1):
#         q.enqueue(i)
#         print("Peeking:", q.peek())
#         print("Queue =", q)
#
#     print("Length:", len(q))
#     print("Empty:", q.is_empty())
#     while not q.is_empty():
#         print("Peeking:", q.peek())
#         q.dequeue()
#         print("Queue =", q)
#
#     print("Length:", len(q))
#     print("Empty:", q.is_empty())
