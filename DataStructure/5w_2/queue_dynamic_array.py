class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("queue is empty.")
        self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("queue is empty.")
        return self.items[-1]

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        pos = 0
        while pos < len(self):
            yield self.items[pos]
            pos += 1

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    queue = Queue()
    print("Len:", len(queue))
    print("Is Empty:", queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue)
    print("Len:", len(queue), queue)
    print("Is Empty:", queue.is_empty())
    print("Peek:", queue.peek())
    queue.dequeue()
    print("Peek:", queue.peek())
    queue.dequeue()
    print("Len:", len(queue), queue)
    print()
    N = 5
    for i in range(1, N + 1):
        queue.enqueue(i)
    print("Len:", len(queue), queue)
    while not queue.is_empty():
        print("Peek:", queue.peek(), "Len:", len(queue), queue)
        queue.dequeue()
    print("Len:", len(queue), queue)