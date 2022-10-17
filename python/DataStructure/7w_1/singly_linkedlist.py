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


class SinglyLinkedList:
    def __init__(self):
        self.head = self.next_ = None  # Node next difference with List next_

    def __iter__(self):
        return self

    # def __next__(self):
    #     if self.next_ is not None:
    #         temp = self.next_
    #         self.next_ = self.next_.next
    #         return temp
    #     else:
    #         raise StopIteration

    def __next__(self):
        if self.next_ is not None:
            temp = self.next_
            self.next_ = self.next_.next
            return temp
        else:
            self.next_ = self.head
            raise StopIteration

    def add_head(self, node_new):
        new_node = self.next_ = Node(node_new)

        if self.head is None:
            self.head = new_node
        else:
            tmp = self.head
            self.head = new_node
            self.head.next = tmp

    def add_tail(self, node_new):
        new_node = Node(node_new)

        if self.head is None:
            self.head = new_node
        else:
            iterator = self.head
            while iterator.next is not None:
                iterator = iterator.next
            iterator.next = new_node

    def delete_tail(self):
        iterator = self.head

        if iterator is None:
            raise Exception("List is empty")
        elif iterator.next is None:
            self.head = None
        else:
            while iterator.next.next is not None:
                iterator = iterator.next
            iterator.next = None

    def delete_head(self):
        if self.head is None:
            raise Exception("List is empty")
        elif self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.next_ = self.head

    def insert_after(self, node, node_new):
        new_node = Node(node_new)
        iterator = self.head

        while iterator != Node(node):
            iterator = iterator.next
        new_node.next = iterator.next
        iterator.next = new_node

    def insert_before(self, node, node_new):
        new_node = Node(node_new)
        iterator = self.head

        if iterator == Node(node):
            self.add_head(new_node)
        else:
            while iterator.next != Node(node):
                iterator = iterator.next
            # temp = iterator.next
            # iterator.next = new_node
            # new_node.next = temp

            new_node.next = iterator.next
            iterator.next = new_node

    def delete(self, node):
        node = Node(node)
        iterator = self.head

        if iterator == node:
            self.delete_head()
        else:
            while iterator.next.item != node.item:
                iterator = iterator.next
            temp = iterator
            iterator.next = iterator.next.next
            temp = None

    def __str__(self):
        result = "["
        iterator = self.head

        while iterator is not None:
            result += str(iterator)
            iterator = iterator.next
            if iterator is not None:
                result += ", "

        result += "]"
        return result


# list_ = SinglyLinkedList()
# list_.add_head(Node(50))
# list_.add_tail(Node(100))
# list_.add_tail(Node(150))
# print("1", list_)
#
# list_.delete_head()
# print("2", list_)
# list_.delete_tail()
# print("3", list_)
# list_.delete_head()
# print("4", list_)
#
# list_.add_tail(Node(150))
# list_.add_tail(Node(300))
# list_.insert_before(Node(300), Node(999))
# print("5", list_)
#
# list_.add_head(Node(50))
# list_.add_tail(Node(100))
# print("6", list_)

# for i in list_:
#     print("Element:", i)
#
# list_.add_tail(Node(700))
# print("7", list_)
#
# list_.insert_after(Node(1), Node(30))
# print("8", list_)

# list_.insert_before(Node(150), Node(10))
# print("9", list_)
#
# list_.delete(Node(50))
# print("10", list_)
#
# for i in list_:
#     print("Element:", i)
