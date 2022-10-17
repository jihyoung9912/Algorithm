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
        raise NotImplemented

    def add_tail(self, node_new):
        tmp = self.head
        if self.head is None:
            self.head = node_new
        elif self.head.llink is None:
            self.head.rlink = node_new
            self.head.llink = node_new
            node_new.llink = self.head
            node_new.rlink = self.head
        else:
            while self.head.rlink is not tmp:
                self.head = self.head.rlink
            self.head.rlink = node_new
            node_new.llink = self.head
            node_new.rlink = tmp


    def delete_head(self):
        if self.is_empty():
            raise Exception("list is empty.")
        raise NotImplemented

    def delete_tail(self):
        if self.is_empty():
            raise Exception("list is empty.")
        raise NotImplemented

    def insert_before(self, node, node_new):
        if self.is_empty():
            raise Exception("list is empty.")
        raise NotImplemented

    def insert_after(self, node, node_new):
        if self.is_empty():
            raise Exception("list is empty.")
        raise NotImplemented

    def delete(self, node):
        if self.is_empty():
            raise Exception("list is empty.")
        raise NotImplemented

    def __iter__(self):
        raise NotImplemented

    def __next__(self):
        raise NotImplemented

    def is_empty(self):
        raise NotImplemented

    def __str__(self):
        result = "["
        if self.head is None:
            result += "]"
        else:
            if self.head.rlink is None:
                result += str(self.head) + "]"
            else:
                tmp = self.head
                while self.head.rlink is not tmp:
                    result += str(tmp)
                    if self.head.rlink is not tmp:
                        result += ", "
                    self.head = self.head.rlink
                    if self.head.rlink is tmp:
                        result += f"{self.head}]"
        return result


list_ = CircularDoublyLinkedList()
list_.add_tail(Node(10))
list_.add_tail(Node(20))
# list_.add_tail(Node(50))
# list_.add_head(Node(30))
print(list_)
# for i in list_:
#     print("Element:", i)
# print()
# it = iter(list_)
# while True:
#     try:
#         i = next(it)
#     except StopIteration:
#         break
#     print("Element:", i)
# print(list_)
# while not list_.is_empty():
#     list_.delete_tail()
#     print(list_)
# list_.add_tail(Node(20))
# list_.add_head(Node(30))
# print(list_)
# list_.insert_after(Node(30), Node(40))
# list_.insert_before(Node(20), Node(10))
# print(list_)
# list_.delete(Node(40))
# print(list_)
# list_.delete(Node(30))
# print(list_)
# list_.delete(Node(20))
# print(list_)