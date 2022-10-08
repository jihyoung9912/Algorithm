from arrays import Array


class Stack:
    CAPACITY = 10

    def __init__(self, capacity=CAPACITY):
        self.arr = Array(capacity)
        self.capacity = capacity
        self.top = -1

    def is_full(self):
        return len(self) >= self.capacity

    def is_empty(self):
        return len(self) <= 0

    def push(self, elem):
        if self.is_full():
            raise Exception("Stack is Full")
        else:
            self.top += 1
            self.arr[self.top] = elem

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        else:
            val = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return val

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        else:
            return self.arr[self.top]

    def __len__(self):
        return self.top + 1

    def __iter__(self):
        pos = 0
        while pos < len(self):
            yield self.arr[pos]
            pos += 1

    def __str__(self):
        return str(self.arr)
