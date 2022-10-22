class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)


def verify_parentheses(expr):
    stack = Stack()
    for i in expr:
        if i == "(":
            stack.push(i)
        elif i == ")":
            if stack.is_empty():
                return False
            else:
                stack.pop()
    return stack.is_empty()


if __name__ == "__main__":
    sexpr = "((()"
    res = verify_parentheses(sexpr)
    print(res)

    sexpr = "(()())"
    res = verify_parentheses(sexpr)
    print(res)

    sexpr = "((()))())"
    res = verify_parentheses(sexpr)
    print(res)