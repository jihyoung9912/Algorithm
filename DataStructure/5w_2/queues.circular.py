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
        self.front += 1
        return self.arr[self.front]

    def __len__(self):
        raise NotImplemented

    def __str__(self):
        return str(self.arr)

    def __iter__(self):
        raise NotImplemented

    def __iter__(self):
        raise NotImplemented

    def enqueue(self, elem):
        tmp = (self.rear + 1) % 8
        self.arr[tmp] = elem
        self.rear += 1

    def dequeue(self):
        self.arr[self.front] = None


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
    # for i in queue:
    #     print("Element:", i)
    # print("Peek:", queue.peek())
    # while not queue.is_empty():
    #     queue.dequeue()
    # print(queue)