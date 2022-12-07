class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, elem):
        self.items.append(elem)

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty.")
        self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("stack is empty.")
        return self.items[-1]

    def __iter__(self):
        pos = 0
        while pos < len(self):
            yield self.items[pos]
        pos += 1

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class HeadNode:
    def __init__(self, id_=0, degree=0):
        self.id_ = id_
        self.degree = degree  # as indegree
        self.link = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.id_}"


class Node:
    def __init__(self, vertex=0, duration=0):
        self.vertex = vertex
        self.duration = duration
        self.link = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.vertex, self.duration}"
