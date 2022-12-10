from singly_linkedlist import SinglyLinkedList, Node


class Stack:
    def __init__(self):
        self.list_ = SinglyLinkedList()

    def push(self, elem):
        self.list_.add_tail(elem)

    def pop(self):
        if self.list_.head is None:
            raise Exception("List is empty")
        else:
            self.list_.delete_tail()

    def peek(self):
        tmp = self.list_.head
        if self.list_.head is None:
            raise Exception("List is empty")
        else:
            while tmp.next is not None:
                tmp = tmp.next
            return tmp

    def is_empty(self):
        return self.list_.head is None

    def __iter__(self):
        self.list_.next_ = self.list_.head
        return self.list_

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
print(stack.is_empty())
while not stack.is_empty():
    print("peek:", stack.peek())
    stack.pop()
    print(stack)
