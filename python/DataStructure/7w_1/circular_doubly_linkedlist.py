class Node:
    def __init__(self, item=None):
        self.item = item
        self.llink = self.rlink = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        if self is other or self.item == other.item:
            return True
        return False

    def __str__(self):
        return f"{self.item}"

    def __repr__(self):
        return str(self)


class CircularDoublyLinkedList:
    """class Doubly linked list"""

    def __init__(self):
        self.head = None

    def add_head(self, node_new):
        tmp = self.head
        if self.head is None:
            self.head = node_new
        elif self.head.llink is None:
            self.head = node_new
            self.head.rlink = tmp
            tmp.llink = self.head
            tmp.rlink = self.head
            self.head.llink = tmp
        else:
            self.head = node_new
            node_new.rlink = tmp
            node_new.llink = tmp.llink
            tmp.llink.rlink = node_new
            tmp.llink = node_new

    def add_tail(self, node_new):
        tmp = self.head
        if self.head is None:  # 빈 배열일 때
            self.head = node_new
        elif self.head.llink is None:  # 하나의 원소만 존재할 경우
            self.head.rlink = node_new
            self.head.llink = node_new
            node_new.llink = self.head
            node_new.rlink = self.head
        else:
            while tmp.rlink is not self.head:
                tmp = tmp.rlink
            tmp.rlink = node_new
            node_new.llink = tmp
            node_new.rlink = self.head
            self.head.llink = node_new

    def delete_head(self):
        if self.is_empty():
            raise Exception("list is empty.")
        elif self.head.rlink is None:
            self.head = None
        else:
            tmp = self.head
            tmp.rlink.llink = tmp.llink
            tmp.llink.rlink = tmp.rlink
            self.head = tmp.rlink
            if self.head.rlink == self.head:
                self.head.rlink = self.head.llink = None

    def delete_tail(self):
        if self.is_empty():
            raise Exception("list is empty.")
        else:
            tmp = self.head
            if self.head.rlink is None:
                self.head = None
            elif self.head.rlink.rlink is self.head:
                self.head.llink, self.head.rlink = None, None
            else:
                while tmp.rlink.rlink is not self.head:
                    tmp = tmp.rlink
                tmp.rlink = self.head
                self.head.llink = tmp

    def insert_before(self, node, node_new):
        if self.is_empty():
            raise Exception("list is empty.")
        elif self.head.rlink is None:
            self.add_head(node_new)
        else:
            tmp = self.head
            while tmp.rlink != node:
                tmp = tmp.rlink
            if tmp.rlink == self.head:
                self.add_head(node_new)
            else:
                node_new.llink = tmp
                node_new.rlink = tmp.rlink
                tmp.rlink.llink = node_new
                tmp.rlink = node_new

    def insert_after(self, node, node_new):
        if self.is_empty():
            raise Exception("list is empty.")
        elif self.head.rlink is None:
            self.add_tail(node_new)
        else:
            tmp = self.head
            while tmp != node:
                tmp = tmp.rlink
            node_new.llink = tmp
            node_new.rlink = tmp.rlink
            tmp.rlink.llink = node_new
            tmp.rlink = node_new

    def delete(self, node):
        if self.is_empty():
            raise Exception("list is empty.")
        else:
            if node == self.head:
                self.delete_head()
            elif node == self.head.llink:
                self.delete_tail()
            else:
                tmp = self.head
                while tmp != node:
                    tmp = tmp.rlink
                tmp.llink.rlink = tmp.rlink
                tmp.rlink.llink = tmp.llink

    def __iter__(self):
        self.tmp = self.head
        self.count = 0
        return self

    def __next__(self):
        if self.head.rlink is None:
            return self.head
        else:
            if self.tmp.rlink is not self.head:
                temp = self.tmp
                self.tmp = self.tmp.rlink
                return temp
            elif self.tmp.rlink is self.head and self.count == 0:
                self.count += 1
                return self.tmp
            elif self.tmp.rlink is self.head and self.count == 1:
                self.tmp = self.tmp.rlink
                raise StopIteration

    def is_empty(self):
        return not bool(self.head)

    def __str__(self):
        result = "["
        if self.head is None:
            result += "]"
        else:
            if self.head.rlink is None:
                result += str(self.head) + "]"
            else:
                tmp = self.head
                while tmp.rlink is not self.head:
                    result += str(tmp)
                    if tmp.rlink is not tmp:
                        result += ", "
                    tmp = tmp.rlink
                    if tmp.rlink is self.head:
                        result += f"{tmp}]"
        return result


list_ = CircularDoublyLinkedList()
list_.add_tail(Node(10))
list_.add_tail(Node(20))
list_.add_head(Node(30))
print(list_)
for i in list_:
    print("Element:", i)
print()
it = iter(list_)
while True:
    try:
        i = next(it)
    except StopIteration:
        break
    print("Element:", i)
print(list_)
while not list_.is_empty():
    list_.delete_tail()
    print(list_)
list_.add_tail(Node(20))
list_.add_head(Node(30))
print(list_)
list_.insert_after(Node(20), Node(40))
list_.insert_before(Node(30), Node(10))
print(list_)
list_.delete(Node(40))
print(list_)
list_.delete_head()
print(list_)
list_.delete(Node(20))
print(list_)
list_.delete(Node(30))
print(list_)
