from stacks import Stack


class Infix:
    OPS = ["+", "-", "*", "/", "^"]
    parenthesis = ["(", ")"]

    def __init__(self, expr):
        (*self.expr,) = expr

    def translate_postfix(self):
        stack = Stack(len(self.expr))
        list_ = []
        for token in self.expr:
            if token not in self.OPS and token not in self.parenthesis:  # operand
                list_.append(token)
            elif token == self.parenthesis[0]:  # opening parenthesis
                stack.push(token)
            elif token in self.OPS:  # operator
                if stack.is_empty() or stack.peek() == self.parenthesis[0]:  # stack 이 비어 있거나 stack.peek가 여는 괄호
                    stack.push(token)
                elif self.operator_priority(token) > self.operator_priority(stack.peek()):  # priority 고려
                    stack.push(token)
                else:
                    list_.append(stack.pop())
                    stack.push(token)
            elif token == self.parenthesis[1]:  # 닫힌 괄호
                popped = stack.pop()
                while popped != self.parenthesis[0]:  # 열린 괄호가 나올때까지 반복
                    list_.append(popped)
                    popped = stack.pop()  # 열린괄호가 나오고 pop 하면 열린괄호는 discard 된다.
        while not stack.is_empty():  # stack 에 남은거
            list_.append(stack.pop())

        return "".join(list_)

    def operator_priority(self, token):
        return self.OPS.index(token) // 2


if __name__ == "__main__":
    expr = "a*(b+c)*d"
    infix = Infix(expr)
    postfix = infix.translate_postfix()
    print(postfix)
