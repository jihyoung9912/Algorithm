from circular_doubly_linkedlist import Node, CircularDoublyLinkedList


class Stack:
    def __init__(self):
        self.list_ = CircularDoublyLinkedList()

    def push(self, elem):
        self.list_.add_head(Node(elem))

    def pop(self):
        self.list_.delete_head()

    def peek(self):
        if self.is_empty():
            raise Exception("List is empty")
        elif self.list_.head.rlink is None:
            return self.list_.head
        else:
            return self.list_.head

    def is_empty(self):
        return self.list_.is_empty()

    def __iter__(self):
        return iter(self.list_)

    def __str__(self):
        return f"{self.list_}"


stack = Stack()
stack.push(10)
stack.push(20)
print(stack)
print("peek:", stack.peek())
stack.pop()
print(stack)
stack.push(30)
print(stack)
stack.push(40)
print(stack)
print("peek:", stack.peek())
stack.pop()
print(stack)

for i in stack:
    print("Element:", i)

print()
print(stack)
while not stack.is_empty():
    print("peek:", stack.peek())
    stack.pop()
    print(stack)