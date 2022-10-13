class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        if self is other or self.item == other.item:
            return True

        return False

    def __str__(self):
        return f"{self.item}"


class CircularSinglyLinkedList:
    def __init__(self):
        self.tail = None

    def add_head(self, node_new):
        new_node = Node(node_new)

        if self.tail is None:
            self.tail = new_node
            self.tail.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node

    def add_tail(self, node_new):
        new_node = Node(node_new)

        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def delete_tail(self):
        if self.tail.next is not None:
            if self.tail is self.tail.next:
                self.tail = None
            else:
                temp = self.tail
                while temp.next is not self.tail:
                    temp = temp.next
                temp.next = self.tail.next
                self.tail = temp

    def delete_head(self):
        if self.tail.next is not None:
            if self.tail is self.tail.next:
                self.tail = None
            else:
                tmp = self.tail.next
                self.tail.next = self.tail.next.next
                tmp = None

    def insert_after(self, node, node_new):
        new_node = Node(node_new)

        temp = self.tail
        if temp is temp.next:
            temp.next = new_node
            self.tail = new_node
        elif temp == Node(node):
            self.add_tail(new_node)
        else:
            while temp != Node(node):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def insert_before(self, node, node_new):
        new_node = Node(node_new)

        temp = self.tail
        while temp.next != Node(node):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    # def delete(self, node):

    def __str__(self):
        result = "["

        if self.tail is None:
            return "[]"
        else:
            head = self.tail.next
            if self.tail == head:
                result += str(head) + "]"
                return result
            else:
                while head is not self.tail:
                    result += str(head)
                    head = head.next
                    if head is not self.tail:
                        result += ", "
                result += ", " + str(self.tail) + "]"
                return result


list_ = CircularSinglyLinkedList()
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
list_.insert_before(Node(300), Node(999))
print("6", list_)

list_.add_head(Node(50))
list_.add_tail(Node(100))
print("6", list_)
#
list_.add_tail(Node(700))
print("7", list_)
#
list_.insert_after(Node(999), Node(250))
print("8", list_)
#
