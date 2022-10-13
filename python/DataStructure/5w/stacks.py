from array import Array


class Stack:
    CAPACITY = 10

    def __init__(self, capacity=CAPACITY):
        self.arr = Array(capacity)
        self.capacity = capacity
        self.top = -1

    def is_full(self):
        return len(self) >= self.capacity

    def is_empty(self):
        return not len(self)

    def push(self, elem):
        if self.is_full():
            raise Exception("Stack is full")
        self.top += 1
        self.arr[self.top] = elem

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        self.arr[self.top] = None
        self.top -= 1

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
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

N = 4
stack = Stack(N)
print("Length:", len(stack))
print("Is Empty:", stack.is_empty())
print("Push from 1 to", N)
for i in range(1, N + 1):
    print("Push:", i)
    stack.push(i)
    print("Stack:", stack)
    print("Peek:", stack.peek())
print("Is Empty:", stack.is_empty())
for i in stack:
    print("Element:", i)
print()
for i in range(N):
    print("Peek and Pop: ", stack.peek())
    stack.pop()
    print("Stack:", stack)
print("Length:", len(stack))
print("Is Empty:", stack.is_empty())
