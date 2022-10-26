class Node:
    def __init__(self, item = None):
        self.item = item
        self.rlink = self.llink = None

    def __str__(self):
        return f"{self.item}"

    def __repr__(self):
        return str(self)


class Queue:
    def __init__(self):
        self.header = Node()
        self.header.llink = self.header.rlink = self.header

    def enqueue(self, item):
        node = Node(item)

        if self.header.item is None:
            self.header = node
            self.header.llink = self.header.rlink = self.header
        else:
            tmp = self.header
            while tmp.rlink != self.header:
                tmp = tmp.rlink
            tmp.rlink = node
            node.llink = tmp
            node.rlink = self.header
            self.header.llink = node

    def dequeue(self):
        if self.header.item is None:
            raise Exception("Queue is empty")
        else:
            if self.header.rlink == self.header:
                self.header = Node()
                self.header.llink = self.header.rlink = self.header
            tmp = self.header
            self.header = self.header.rlink
            self.header.llink = tmp.llink
            tmp.llink.rlink = self.header
            return tmp.item

    def peek(self):
        print(self.header.item)

    def __str__(self):
        ret = []
        tmp = self.header
        while tmp.rlink != self.header:
            ret.append(tmp.item)
            tmp = tmp.rlink
        if tmp.item is not None:
            ret.append(tmp.item)
        return str(ret)


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q)
q.peek()
q.dequeue()
q.dequeue()
q.dequeue()
print(q)