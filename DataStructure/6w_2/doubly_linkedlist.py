class Node:
    def __init__(self, item=None):
        self.item = item
        self.rlink = self.llink = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        if self is other or self.item == other.item:
            return True

        return False

    def __str__(self):
        return f"{self.item}"


class DoublyLinkedList:
    def __init__(self):
        self.tail = None

    def add_head(self, node_new):
        new_node = Node(node_new)

        if self.tail is None:
            self.tail = new_node
        else:
            tmp = self.tail
            while self.tail.llink is not None:
                self.tail = self.tail.llink
            self.tail.llink = new_node
            new_node.rlink = self.tail
            self.tail = tmp

    def add_tail(self, node_new):
        new_node = Node(node_new)

        if self.tail is None:
            self.tail = new_node
        else:
            self.tail.rlink = new_node
            new_node.llink = self.tail
            self.tail = new_node

    def delete_head(self):
        if self.tail is None:
            raise Exception("List is empty")
        elif self.tail.llink is None:
            self.tail = None
        else:
            tmp = self.tail
            while self.tail.llink.llink is not None:
                self.tail = self.tail.llink
            self.tail.llink = None
            self.tail = tmp

    def delete_tail(self):
        if self.tail is None:
            raise Exception("List is empty")
        elif self.tail.llink is None:
            self.tail = None
        else:
            tmp = self.tail
            self.tail = self.tail.llink
            self.tail.rlink = None
            tmp = None

    def insert_before(self, node, node_new):
        new_node = Node(node_new)

    def insert_after(self, node, node_new):
        new_node = Node(node_new)

        if self.tail == Node(node):
            self.add_tail(new_node)
        else:
            tmp = self.tail
            while self.tail != Node(node):
                self.tail = self.tail.llink
            temp = self.tail.rlink
            self.tail.rlink = new_node
            new_node.rlink = temp
            self.tail = tmp

    def __str__(self):
        result = "["
        if self.tail is None:
            result += "]"
        else:
            if self.tail.llink is None:
                result += str(self.tail) + "]"
            else:
                while self.tail.llink is not None:
                    self.tail = self.tail.llink
                while self.tail.rlink is not None:
                    result += str(self.tail)
                    self.tail = self.tail.rlink
                    if self.tail.rlink is not None:
                        result += ", "
                result += ", " + str(self.tail) + "]"
        return result


list_ = DoublyLinkedList()
list_.add_head(Node(300))
list_.add_head(Node(400))
list_.add_head(Node(500))
list_.add_tail(Node(200))
list_.add_tail(Node(100))
print("1", list_)

list_.delete_head()
print("2", list_)
list_.delete_tail()
print("3", list_)
list_.delete_head()
print("4", list_)

list_.add_tail(Node(100))
list_.add_tail(Node(10))
print("5", list_)

list_.insert_before(Node(200), Node(999))
print("6", list_)

# list_.add_head(Node(1000))
# list_.add_tail(Node(1))
# print("7", list_)
#
# list_.insert_after(Node(1000), Node(0))
# print("8", list_)
